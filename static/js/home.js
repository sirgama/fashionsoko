console.log('hello world')
var updateBtns = document.getElementsByClassName('update-cart')

for (var i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log(productId, action)
        console.log(user)

        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        }else {
            updateOrder(productId, action)
            location.reload()
        }

    })
}
function updateOrder(productId, action){
    console.log('user is logged in')
    location.reload()
    var url = '/shop/update_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })
    .then((response) =>{
        return response.json()
        location.reload()
    })
    .then((data) =>{
        console.log('data', data)
        location.reload()
    })
}
