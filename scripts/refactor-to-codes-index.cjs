const fs = require('fs');
const path = require('path');

const jsonPath = path.join(__dirname, '../src/data/study-schedule.json');
const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));

// Create codes index from subjects
const codes = {};

Object.keys(data.subjects).forEach(subject => {
  data.subjects[subject].forEach(item => {
    codes[item.code] = {
      title: item.title,
      themes: item.keys,
      subject: subject
    };
  });
});

// Refactor schedule to only store codes
const newSchedule = {};

Object.keys(data.schedule).forEach(date => {
  newSchedule[date] = data.schedule[date].map(task => task.code);
});

// Build new structure
const newData = {
  codes: codes,
  themes: data.themes,
  subjects: data.subjects,
  schedule: newSchedule
};

fs.writeFileSync(jsonPath, JSON.stringify(newData, null, 2));
console.log('Refactored JSON structure');
console.log('- Codes index:', Object.keys(codes).length, 'entries');
console.log('- Schedule now stores only code arrays');
