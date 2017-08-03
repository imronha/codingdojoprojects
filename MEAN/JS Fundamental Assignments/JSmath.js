function zero_negativity(arr){
  for (var i = 0; i<arr.length-1; i++){
    if(arr[i] % 2 ===0){
      return true;
    }
    return false;
  }
}
zero_negativity([1,2,3,4,5,6]);
zero_negativity([2,4,6,8,10]);

function is_even(num){
  if(num%2 ===0){
    return true;
  }
  return false;
}

is_even(5)
is_even(6)

function how_many_even(arr){
  var count = 0;
  for(var i = 0; i<arr.length; i++){
    if(is_even(arr[i])){
      count +=1;
      console.log(i);
    }
  }
  return count
}

how_many_even([1,2,3,4])

function create_dummy_array(n){
  var arr = [];
  for(var i=0; i<n; i++){
    arr.push(Math.floor(Math.random()*10))
  }
  return arr
}

create_dummy_array(8)

function random_choice(arr){
  return arr[Math.floor(Math.random()*(arr.length-0))]
}

random_choice([1,2,3,4])
