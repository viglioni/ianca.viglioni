const fs = require('fs');
const path = require('path');

const jsonPath = path.join(__dirname, '../src/data/study-schedule.json');
const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));

// Mapping: old week -> new week
const weekMapping = {
  '1': '1',
  'ferias': '2',
  '2': '3',
  '3': '4'
};

// Update codes keys
const newCodes = {};
Object.keys(data.codes).forEach(oldCode => {
  // Parse code: mat-ferias-1 -> mat-2-1
  const parts = oldCode.split('-');
  if (parts.length >= 3) {
    const subject = parts[0];
    const oldWeek = parts[1];
    const number = parts[2];
    const newWeek = weekMapping[oldWeek] || oldWeek;
    const newCode = `${subject}-${newWeek}-${number}`;

    newCodes[newCode] = data.codes[oldCode];
  } else {
    newCodes[oldCode] = data.codes[oldCode];
  }
});

data.codes = newCodes;

// Update schedule dates
const newSchedule = {};
Object.keys(data.schedule).forEach(date => {
  const oldCodes = data.schedule[date];
  const newCodesList = oldCodes.map(oldCode => {
    const parts = oldCode.split('-');
    if (parts.length >= 3) {
      const subject = parts[0];
      const oldWeek = parts[1];
      const number = parts[2];
      const newWeek = weekMapping[oldWeek] || oldWeek;
      return `${subject}-${newWeek}-${number}`;
    }
    return oldCode;
  });
  newSchedule[date] = newCodesList;
});

data.schedule = newSchedule;

// Update subjects
Object.keys(data.subjects).forEach(subject => {
  data.subjects[subject] = data.subjects[subject].map(item => {
    const oldCode = item.code;
    const parts = oldCode.split('-');
    if (parts.length >= 3) {
      const subj = parts[0];
      const oldWeek = parts[1];
      const number = parts[2];
      const newWeek = weekMapping[oldWeek] || oldWeek;
      const newCode = `${subj}-${newWeek}-${number}`;
      return {
        ...item,
        code: newCode
      };
    }
    return item;
  });
});

// Update themes
Object.keys(data.themes).forEach(theme => {
  data.themes[theme].codes = data.themes[theme].codes.map(codeObj => {
    const oldCode = codeObj.code;
    const parts = oldCode.split('-');
    if (parts.length >= 3) {
      const subject = parts[0];
      const oldWeek = parts[1];
      const number = parts[2];
      const newWeek = weekMapping[oldWeek] || oldWeek;
      const newCode = `${subject}-${newWeek}-${number}`;
      return { code: newCode };
    }
    return codeObj;
  });
});

fs.writeFileSync(jsonPath, JSON.stringify(data, null, 2));
console.log('Updated database:');
console.log('- Semana 1 → 1 (unchanged)');
console.log('- Férias → 2');
console.log('- Semana 2 → 3');
console.log('- Semana 3 → 4');
console.log('Total codes updated:', Object.keys(data.codes).length);
