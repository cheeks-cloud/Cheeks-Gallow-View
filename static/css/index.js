$(document).ready(function () {
  $('.info').hide()

  $('.image').on('click', function() {
      $(this).children('.image').addClass('blur')
      $(this).children('.info').fadeIn( "slow")
  })

  $('.image').on('click', function() {
      $(this).children('.image').removeClass('blur')
      $(this).children('.info').fadeOut( "slow")
  })
})

function copy_url(data){
  navigator.clipboard.writeText(window.location.origin + data)
}