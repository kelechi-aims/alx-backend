// Import necessary modules
import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

// Use test mode for the Kue queue
const queue = kue.createQueue();

// Define test suite for createPushNotificationsJobs function
describe('createPushNotificationsJobs', () => {
  before(() => {queue.testMode.enter()});
  afterEach(() => {queue.testMode.clear()});
  after(() => {queue.testMode.exit();});

  // Define test case for error message if jobs is not an array
  it('display a error message if jobs is not an array', (done) => {
    try {
      createPushNotificationsJobs({}, queue);
      done(new Error('Expected an error to be thrown.'));
    } catch (error) {
      expect(error.message).to.equal('Jobs is not an array');
      done();
    }
  });

  // Define test case for creating two new jobs to the queue
  it('create two new jobs to the queue', () => {
    const list = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' }
    ];

    createPushNotificationsJobs(list, queue);

    // Validate the jobs in the queue
    expect(queue.testMode.jobs.length).to.equal(2);

    const job1 = queue.testMode.jobs[0];
    const job2 = queue.testMode.jobs[1];
	  
    expect(job1.type).to.equal('push_notification_code_3');
    expect(job1.data.phoneNumber).to.equal('4153518780');
    expect(job1.data.message).to.equal('This is the code 1234 to verify your account');

    expect(job2.type).to.equal('push_notification_code_3');
    expect(job2.data.phoneNumber).to.equal('4153518781');
    expect(job2.data.message).to.equal('This is the code 4562 to verify your account');
  });
});
