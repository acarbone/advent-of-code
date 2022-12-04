const fs = require('fs/promises');

const readFrominputTxt = async () => {
  try {
    return await fs.readFile('./input.txt', { encoding: 'utf8' });
  } catch (err) {
    console.log(err);
  }
}

class Assignment {
  constructor(range) {
    this.range = range;
    let edges = this.range.split('-');

    this.left = parseInt(edges[0]);
    this.right = parseInt(edges[1]);
  }

  contains(assignment) {
    return this.left <= assignment.left && this.right >= assignment.right;
  }
}

const getAssignments = (record) => {
  let assignments = record.split(',');
  let left = new Assignment(assignments[0]);
  let right = new Assignment(assignments[1]);

  return {
    left,
    right
  };
}


const execute = async () => {
  let input = await readFrominputTxt();
  const records = input.split('\n');
  let amount = records.reduce((accumulator, record) => {
    if (record.length === 0) {
      return accumulator;
    }

    let assignments = getAssignments(record);

    let overlaps = assignments.left.contains(assignments.right) || assignments.right.contains(assignments.left);

    if (overlaps) {
      console.log(assignments);
      accumulator++;
    }

    return accumulator;
  }, 0);

  console.log(`\nThe total amount of overlapping assignments is ${amount}`);
}

execute();
