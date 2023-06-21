const redis = require('redis');
const client = redis.createClient();
const util = require('util')

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));
function setNewSchool(schoolName, value){
   client.set(schoolName, value, redis.print)
};
util.promisify (displaySchoolValue(schoolName)
await client.get(schoolName, function (err, reply) {
  console.log(reply);
});

};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

