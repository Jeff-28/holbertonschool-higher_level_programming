$(function () {
  $('#btn_translate').click(function () {
    const code = $('#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + code, function (response) {
      $('#hello').text(response.hello);
    });
  });
});
