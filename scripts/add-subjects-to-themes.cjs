const fs = require('fs');
const path = require('path');

const jsonPath = path.join(__dirname, '../src/data/study-schedule.json');
const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));

// Update themes to include subject information
const themesWithSubjects = {};

Object.keys(data.themes).forEach(theme => {
  const codes = data.themes[theme];
  const subjects = new Set();

  codes.forEach(codeObj => {
    const codeData = data.codes[codeObj.code];
    if (codeData && codeData.subject) {
      subjects.add(codeData.subject);
    }
  });

  themesWithSubjects[theme] = {
    codes: codes,
    subjects: Array.from(subjects).sort()
  };
});

data.themes = themesWithSubjects;

fs.writeFileSync(jsonPath, JSON.stringify(data, null, 2));
console.log('Updated themes with subject information');
console.log('Sample:', Object.keys(themesWithSubjects).slice(0, 3).map(k => ({
  theme: k,
  subjects: themesWithSubjects[k].subjects
})));
