// Import the required modules
import kue from 'kue';

// Define the function to create push notifications jobs
function createPushNotificationsJobs(jobs, queue) {
  // Check if jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Iterate over each job in the jobs array
  jobs.forEach((jobData) => {
    // Create a job in the queue push_notification_code_3
    const job = queue.create('push_notification_code_3', jobData);

    // Create jobs in the queue
    job.save((error) => {
      if (!error) {
        console.log(`Notification job created: ${job.id}`);
      }
    });

    // Listen for job completion
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // Listen for job failure
    job.on('failed', (errorMeassge) => {
      console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    });

    // Listen for job progress
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}

module.exports = createPushNotificationsJobs;
