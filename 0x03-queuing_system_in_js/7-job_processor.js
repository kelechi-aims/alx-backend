// Import the require module
import kue from 'kue';

// Define the array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Define the function to send a notification
function sendNotification(phoneNumber, message, job, done) {
  // Track the progress of the job
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    // If phoneNumber is blacklisted, fail the job
    const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
    job.failed().error(error);
    done(error);
  } else {
    // If phoneNumber is not blacklisted, continue processing the job
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
}

// Create a Kue queue for push_notification_code_2 queue with concurrency 2
const queue = kue.createQueue({ concurrency: 2 });

// Process jobs from the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
