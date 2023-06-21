const redis = require('redis');
const client = redis.createClient();
//client.hmset('HolbertonSchools', 'Portland', '50', 'Seattle', '80', 'New York', '20', 'Bogota', '20', 'Cali', '40', 'Paris', '2', redis.print)
client.hmset('HolbertonSchools', 'Portland', '50', redis.print)
client.hmset('HolbertonSchools', 'Seattle', '80', redis.print)
client.hmset('HolbertonSchools', 'New York', '20', redis.print)
client.hmset('HolbertonSchools', 'Bogota', '20', redis.print)
client.hmset('HolbertonSchools', 'Cali', '40', redis.print)
client.hmset('HolbertonSchools', 'Paris', '2', redis.print)
client.hgetall('HolbertonSchools', function(err, object) {
  console.log(object);
});
