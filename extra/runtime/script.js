document.getElementsByClassName("questions-container")[0].style.overflowY = "scroll"

const textElements = document.querySelectorAll('p, h1, h2, h3, h4, h5, span, div')
textElements.forEach(element => {
    element.style.fontFamily = 'Arial'
})

btn = document.evaluate("//a[contains(@href, 'javascript')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue
if (btn != null) {
    href = btn.getAttribute("href")
    pos1 = href.search("../..")
    pos2 = href.search(",") - 1
    btn.setAttribute("href", href.substring(pos1, pos2))
}

fav_btn = document.getElementsByClassName("favorite-button")[0]
fav_btn.remove()

qblock = document.querySelectorAll("[class^='qblock']")[0];
qblock.style.marginTop = "0px"

answer_button = document.getElementsByClassName('answer-button')[0]
if (answer_button != null) {
    input = document.getElementsByName('answer')[0]
    input.addEventListener('keydown', function(event) {
        if (event.key == 'Enter') {
            answer_button.click()
        }
    })
}
