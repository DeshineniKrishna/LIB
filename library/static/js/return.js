var form4= $('#return'),
    submit4 = form4.find('[name="submit"]');reset4 = form4.find('[name="reset"]');

form4.on('submit', function(e) {
  e.preventDefault();
  
  // avoid spamming buttons
  if (submit4.attr('value') !== 'Send')
    return;
  
  var valid = true;
  form4.find('input, textarea').removeClass('invalid').each(function() {
    if (!this.value) {
      $(this).addClass('invalid');
      valid = false;
    }
  });
  
  if (!valid) {
    form4.animate({left: '-3em'},  50)
        .animate({left:  '3em'}, 100)
        .animate({left:    '0'},  50);
  } else {
    submit4.attr('value', 'Sending...')
          .css({boxShadow: '0 0 200em 200em rgba(225, 225, 225, 0.6)',
                backgroundColor: '#ccc'});
    // simulate AJAX response
    setTimeout(function() {
      // step 1: slide labels and inputs
      // when AJAX responds with success
      // no animation for AJAX failure yet
      form4.find('label')
          .animate({left: '100%'}, 500)
          .animate({opacity: '0'}, 500);
    }, 1000);
    setTimeout(function() {
      // step 2: show thank you message after step 1
      submit4.attr('value', 'Thank you :)')
            .css({boxShadow: 'none'});
    }, 2000);
    setTimeout(function() {
      // step 3: reset
      form4.find('input, textarea').val('');
      form4.find('label')
          .css({left: '0'})
          .animate({opacity: '1'}, 500);
      submit4.attr('value', 'Send')
            .css({backgroundColor: ''});
      reset4.attr('value', 'Reset')
            .css({backgroundColor: ''});
    }, 4000);
  }
});