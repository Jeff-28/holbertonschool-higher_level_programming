$(function () {
  function translate () {
    const code = $('#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + code, function (response) {
      $('#hello').text(response.hello);
    });
  }
  $('#btn_translate').click(translate);
  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      translate();
    }
  });
});
