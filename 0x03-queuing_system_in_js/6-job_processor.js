const kue = require('kue');
const queue = kue.createQueue();

function sendNotification(phoneNumber, message){
  console.log(`Sending notification to PHONE_NUMBER, with message: ${message)`) 
};
