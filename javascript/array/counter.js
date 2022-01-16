s = "naman";

const counter = (s, sMap = {}) => {
  [...s].map((el) => {
    sMap[el] = sMap[el] ? sMap[el] + 1 : 1;
  });
  return sMap;
};

const res = counter(s);
console.log(`res`, res);
