const fs = require('fs/promises');

const readFrominputTxt = async () => {
  try {
    return await fs.readFile('./input.txt', { encoding: 'utf8' });
  } catch (err) {
    console.log(err);
  }
}

const splitInHalves = (item) => {
  const first = item.substring(0, item.length / 2);
  const second = item.substring(item.length / 2, item.length);

  return {
    first,
    second
  }
}

const findCommonItemTypeWithinStrings = (first, second) => {
  for (const letter of first.split('')) {
    if (second.indexOf(letter) !== -1) {
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
  const sum = records.reduce((prev, curr) => {
    if (curr.length === 0) {
      return prev;
    }

    const fragments = splitInHalves(curr);
    const commonItemType = findCommonItemTypeWithinStrings(fragments.first, fragments.second);
    const value = valueItem(commonItemType);

    console.log(curr, fragments.first, fragments.second, commonItemType, value);

    return prev + value;
  }, 0);

  console.log(`\nThe sum of the priorities is: ${sum}`);
}

execute();
