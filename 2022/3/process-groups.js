const fs = require('fs/promises');

const readFrominputTxt = async () => {
  try {
    return await fs.readFile('./input.txt', { encoding: 'utf8' });
  } catch (err) {
    console.log(err);
  }
}

const findCommonItemTypeWithinStrings = (first, second, third) => {
  for (const letter of first.split('')) {
    if (second.indexOf(letter) !== -1 && third.indexOf(letter) !== -1) {
      return letter;
    }
  }
}

const valueItem = (item) => {
  // ASCII Convertion table:
  // a -> 97 -> 1
  // A -> 65 -> 27

  let asciiCode = item.charCodeAt(0);
  // Check if uppercase
  if (asciiCode >= 65 && asciiCode <= 90) {
    return asciiCode - 38;
  }

  // ...otherwise it is lowercase
  return asciiCode - 96;
}

const execute = async () => {
  let input = await readFrominputTxt();
  const records = input.split('\n');

  let index = 0, sum = 0;
  let first, second, third;

  for (record of records) {
    if (record.length === 0) {
      break;
    }

    if (index === 0) {
      first = record;
    } else if(index === 1) {
      second = record;
    } else {
      third = record;

      let commonItemType = findCommonItemTypeWithinStrings(first, second, third);
      let value = valueItem(commonItemType);

      console.log(first, second, third, commonItemType, value);

      sum += value;
      index = -1;
    }

    index++;
  }

  console.log(`\nThe sum of the priorities is: ${sum}`);
}

execute();
