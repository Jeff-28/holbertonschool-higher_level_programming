$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (dict) {
  $('DIV#hello').text(dict.hello);
});
