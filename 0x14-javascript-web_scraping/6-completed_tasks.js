#!/usr/bin/nodejs

const args = process.argv.slice(2);
const request = require('request');
request(args[0], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const tasks = JSON.parse(body);
  const tasksDone = {};
  let id;
  for (const task of tasks) {
    id = task.userId;
    if (task.completed === true) {
      tasksDone[id] = (tasksDone[id] || 0) + 1;
    }
  }
  console.log(tasksDone);
});
