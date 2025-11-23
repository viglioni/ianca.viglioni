const data = require("../src/data/study-schedule.json");

const reduce = (min) => Math.round(min * 0.67 / 5) * 5;

const extraCodes = ["bio-4-2", "bio-4-3", "geo-4-2", "geo-4-3", "hum-4-2", "hum-4-3", "hum-4-4", "hum-4-5", "por-4-1", "fis-4-5", "qui-4-6", "mat-4-7"];

let classes = [];
Object.keys(data.codes).forEach(c => {
  const cl = data.codes[c];
  if (cl.subject === "geral") return;
  if (extraCodes.includes(c)) return;
  classes.push({ code: c, title: cl.title, subject: cl.subject, duration: reduce(cl.duration) });
});

const priority = {"matematica": 1, "fisica": 2, "quimica": 3, "ciencias-humanas": 4, "geografia": 5, "portugues": 6, "filosofia": 7, "sociologia": 8, "biologia": 9};
classes.sort((a,b) => (priority[a.subject] || 99) - (priority[b.subject] || 99) || a.code.localeCompare(b.code));

let currentSubject = "";
classes.forEach(c => {
  if (c.subject !== currentSubject) {
    currentSubject = c.subject;
    console.log("\n=== " + currentSubject.toUpperCase() + " ===");
  }
  console.log(c.duration + "min - " + c.title + " [" + c.code + "]");
});

console.log("\n\nTotal:", classes.reduce((a,b) => a + b.duration, 0) / 60, "hours");
