const fs = require('fs');
const path = require('path');

const jsonPath = path.join(__dirname, '../src/data/study-schedule.json');
const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));

// Add dates to codes by looking at schedule
Object.keys(data.schedule).forEach(date => {
  const codes = data.schedule[date];
  codes.forEach(code => {
    if (data.codes[code]) {
      if (!data.codes[code].dates) {
        data.codes[code].dates = [];
      }
      if (!data.codes[code].dates.includes(date)) {
        data.codes[code].dates.push(date);
      }
    }
  });
});

// Sort dates for each code
Object.keys(data.codes).forEach(code => {
  if (data.codes[code].dates) {
    data.codes[code].dates.sort();
  }
});

fs.writeFileSync(jsonPath, JSON.stringify(data, null, 2));
console.log('Added dates to codes');
console.log('Sample:', Object.keys(data.codes).slice(0, 3).map(k => ({
  code: k,
  dates: data.codes[k].dates
})));
