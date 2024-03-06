const redis = require('redis');
const kue = require('kue')
import { promisify } from 'util';
const express = require('express');

const client = redis.createClient();
const queue = kue.createQueue();
const app = express();
const port = 1245;

function reserveSeat(number) {
  client.set('available_seats', number);
}

const getAsync = promisify(client.get).bind(client);

async function getCurrentAvailableSeats() {
  return await getAsync('available_seats');
}

reserveSeat(50);
let reservationEnabled = true;

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: "Reservation are blocked" });
    return;
  }
  const job = queue.create('reserve_seat');
  job.save((error) => {
    if (error){
      return res.json({ status: "Reservation failed" });
    } else {
      return res.json({ "status": "Reservation in process" });
    }
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });
  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: "Queue processing" });

  queue.process('reserve_seat', async (job, done) => {
    const currentAvailableSeats = await getCurrentAvailableSeats();
    const newAvailableSeats = currentAvailableSeats - 1;

    if (newAvailableSeats === 0) {
      reservationEnabled = false;
    }
    if (newAvailableSeats >= 0) {
      reserveSeat(newAvailableSeats);
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });	
});

app.listen(port);
