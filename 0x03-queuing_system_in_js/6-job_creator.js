const kue = require('kue');
const queue = kue.createQueue();

const jobData = { phoneNumber: '09999299292', message: 'Hello',};

const job = queue.create('push_notification_code', jobData).save((error) => {
  if (error) {
    console.log(`ERROR: ${error}`);
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
});
job.on('completed', () => {
    console.log('Notification job completed');
});
job.on('failed', () => {
    console.log('Notification job failed');
});
