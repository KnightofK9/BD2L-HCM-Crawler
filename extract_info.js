let fs = require('fs');

let contents = fs.readFileSync('web.txt', 'utf8');
let reg_exp = /http:[^"]+\.m3u8/g
let array
while(array = reg_exp.exec(contents)){
  console.log(array);
  break;
}
