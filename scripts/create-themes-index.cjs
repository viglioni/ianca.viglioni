const fs = require('fs');
const path = require('path');

const jsonPath = path.join(__dirname, '../src/data/study-schedule.json');
const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));

// Create themes index
const themes = {};

// Iterate through all subjects
Object.keys(data.subjects).forEach(subject => {
  data.subjects[subject].forEach(item => {
    // For each key in the item, add the code to that theme
    item.keys.forEach(key => {
      if (!themes[key]) {
        themes[key] = [];
      }
      themes[key].push({ code: item.code });
    });
  });
});

// Sort codes within each theme
Object.keys(themes).forEach(theme => {
  themes[theme].sort((a, b) => a.code.localeCompare(b.code));
});

// Sort themes alphabetically
const sortedThemes = {};
Object.keys(themes).sort().forEach(key => {
  sortedThemes[key] = themes[key];
});

// Add themes to the data
data.themes = sortedThemes;

fs.writeFileSync(jsonPath, JSON.stringify(data, null, 2));
console.log('Created themes index with', Object.keys(sortedThemes).length, 'themes');
