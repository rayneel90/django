myNumber.value = commify(myNumber.value)
myNumber.addEventListener("change", function(){
  commify(event.target.value)
})

function commify(value){
  var chars = value.split("").reverse()
  var withCommas = []
  for(var i = 1; i <= chars.length; i++ ){
    withCommas.push(chars[i-1])
    if(i%3==0 && i != chars.length ){
      withCommas.push(",")
    }
  }
  var val = withCommas.reverse().join("")
  myNumber.parentNode.setAttribute("comma-value",val)
}