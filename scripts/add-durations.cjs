const fs = require('fs');
const path = require('path');

const jsonPath = path.join(__dirname, '../src/data/study-schedule.json');
const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));

// Default durations by class position (most classes follow these patterns)
// This is a simplified mapping - you may want to adjust based on your study plan
const defaultDurations = {
  '1': 120,  // First class usually longer
  '2': 90,   // Standard duration
  '3': 90,
  '4': 60,
  '5': 60,
};

// Add duration to each code (default to 90min if not specified)
Object.keys(data.codes).forEach(code => {
  const parts = code.split('-');
  if (parts.length >= 3) {
    const classNumber = parts[2];
    data.codes[code].duration = defaultDurations[classNumber] || 90;
  } else {
    data.codes[code].duration = 90;
  }
});

fs.writeFileSync(jsonPath, JSON.stringify(data, null, 2));
console.log('Added duration field to all codes');
console.log('Sample:', Object.keys(data.codes).slice(0, 3).map(k => ({
  code: k,
  duration: data.codes[k].duration
})));
