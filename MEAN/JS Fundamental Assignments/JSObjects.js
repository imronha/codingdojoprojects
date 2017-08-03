print_emp_man(users)
function print_emp_man(dict){
  for (let i = 0; i<Object.keys(users).length; i++){
    if (i===0){
      console.log("EMPLOYEES");
      for(var j=0; j< dict['employees'].length;j++){
        console.log((j+1)+' '+ dict['employees'][j]['first_name'] + dict['employees'][j]['last_name'] +' - '+ (dict['employees'][j]['first_name'].length + dict['employees'][j]['last_name'].length));
      }
    }
    if (i===1){
      console.log("MANAGERS");
      for(var k=0; k<dict['managers'].length; k++){
        console.log((k+1)+' '+dict['managers'][k]['first_name'] + dict['managers'][k]['last_name'] +' - '+ (dict['managers'][k]['first_name'].length + dict['managers'][k]['last_name'].length));
      }
    }
  }
}
