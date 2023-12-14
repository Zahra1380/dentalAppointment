const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')


const form = document.querySelector('.rate_form')
const confirmBox = document.getElementById('confirm-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const HandelSelect = (selection) => {
    switch (selection) {
        case 'first': {
            one.classList.add('checked')
            two.classList.remove('checked')
            three.classList.remove('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            return
        }

        case 'second': {
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.remove('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            return
        }

        case 'third': {
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.remove('checked')
            five.classList.remove('checked')
            return
        }

        case 'fourth': {
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.add('checked')
            five.classList.remove('checked')
            return
        }

        case 'fifth': {
            one.classList.add('checked')
            two.classList.add('checked')
            three.classList.add('checked')
            four.classList.add('checked')
            five.classList.add('checked')
            return
        }

    }
}

const getNumericValue = (stringValue) => {
    let numericValue;
    if (stringValue === 'first') {
        numericValue = 1
    } else if (stringValue === 'second') {
        numericValue = 2
    } else if (stringValue === 'third') {
        numericValue = 3
    } else if (stringValue === 'fourth') {
        numericValue = 4
    } else if (stringValue === 'fifth') {
        numericValue = 5
    } else {
        numericValue = 0
    }
    return numericValue
}

const arr = [one, two, three, four, five]
if (one) {
    arr.forEach(item => item.addEventListener("mouseover", (event) => {
        HandelSelect(event.target.id)
    }))
    arr.forEach(item => item.addEventListener('click', (event) => {
        const val = event.target.id
        form.addEventListener('submit', e => {
            e.preventDefault()
            const id = e.target.id
            const val_num = getNumericValue(val)

            $.ajax({
                type: 'POST',
                url: '/rating/',
                data: {
                    'csrfmiddlewaretoken': csrf[0].value,
                    'el_id': id,
                    'val': val_num,
                },
                success: function (response){
                    confirmBox.innerHTML = `<span class="border border-success text-success rounded w-50">Successfully rated</span>`
                },
                error: function (error){
                    confirmBox.innerHTML = '<span class="border border-danger text-danger rounded w-50">>Ups... some thing went wrong</span>'
                }
            })
        })
    }))
}