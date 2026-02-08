 $("#id_account").change(function () {
  var url = $("#SaleForm").attr("data-vechile-url");
  var accountId = $(this).val();

  $.ajax({
    url: url,
    data: {
      'account': accountId
    },
    success: function (data) {
      $("#id_vechile").html(data);
    }
  });

});

 $("#id_item").change(function () {
  var url = $("#SaleForm").attr("data-vechile-url");
  var itemId = $(this).val();

  $.ajax({
    url: url,
    data: {
      'item': itemId
    },
    success: function (data) {
      $("#id_rate").html(data);
    }
  });

});