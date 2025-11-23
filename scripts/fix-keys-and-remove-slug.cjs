const fs = require('fs');
const path = require('path');

const jsonPath = path.join(__dirname, '../src/data/study-schedule.json');
const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));

// Function to split and normalize keys
function splitAndNormalizeKeys(keys) {
  const result = new Set();

  keys.forEach(key => {
    // Split by hyphen
    const parts = key.split('-');
    parts.forEach(part => {
      if (part.trim()) {
        result.add(part.trim());
      }
    });
  });

  return Array.from(result).sort();
}

// Fix subjects - split keys and remove slug
Object.keys(data.subjects).forEach(subject => {
  data.subjects[subject] = data.subjects[subject].map(item => {
    const newKeys = splitAndNormalizeKeys(item.keys);
    return {
      code: item.code,
      title: item.title,
      keys: newKeys
    };
  });
});

// Fix schedule - remove slug
Object.keys(data.schedule).forEach(date => {
  data.schedule[date] = data.schedule[date].map(task => ({
    name: task.name,
    subject: task.subject,
    code: task.code
  }));
});

fs.writeFileSync(jsonPath, JSON.stringify(data, null, 2));
console.log('Fixed keys and removed slug field');
