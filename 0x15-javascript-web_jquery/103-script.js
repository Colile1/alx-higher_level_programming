$(document).ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.keyCode === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/';
  $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('DIVhello').html(data.hello);
  });
}
