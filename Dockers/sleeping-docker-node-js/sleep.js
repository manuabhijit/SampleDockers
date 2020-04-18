var d = 1
for (let i = 0; i < 100; i++) {
  for (let index = 0; index < 100000000; index++) {
    d = 1 + index
  }
  console.log(d);
}

