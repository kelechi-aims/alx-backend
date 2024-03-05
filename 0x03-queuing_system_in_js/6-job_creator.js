// Import the required modules
import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Define the job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, world!',
};

// Create a job in the queue
const job = queue.create('push_notification_code', jobData).save((error) => {
  if (!error) console.log(`Notification job created: ${job.id}`);
  });

// Handle job completion event
job.on('complete', () => {
  console.log('Notification job completed');
});

// Handle job failure event
job.on('failed', () => {
  console.log('Notification job failed');
});
