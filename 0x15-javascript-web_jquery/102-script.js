$(document).ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/';
  $('INPUT#btn_translate').click(function () {
    $.get(url + $.param({ lang: $('INPUT#btn_translate').val() }),
      function (data) {
        $('DIV#hello').html(data.hello);
      });
  });
});
