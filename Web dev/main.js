let res;
function f() {
    res = document.getElementsByClassName("init");
    console.log(res[0].value);
};

 function add(val) {
    let init = document.getElementsByClassName("init");
    if (init[0].value==="0") {
        init[0].value = val;
    } else if(val==="kv") {
        init[0].value = init[0].value*init[0].value;
    } else {
        init[0].value = init[0].value + val;
    };
 };

 function result() {
    let calc = document.getElementsByClassName("init");
    calc[0].value = eval(calc[0].value);
 };
