
$(document).ready(function(){
  $('.markdown-content').each(function(){
      var content = $(this).text();
      var markedContent = marked(content);
      $(this).html(markedContent);
  })

  $('.markdown-content img').each(function(){
      $(this).addClass('img-fluid');
  })

  $('.card-text img').each(function(){
    $(this).addClass('img-fluid');
  })

  // creating dynamic preview
  var contentInput = $("#id_content");

  function setContent(value){
    var markedContent = marked(value);
    $("#preview-content").html(markedContent);
    $("#preview-content img").each(function(){
    $(this).addClass('img-fluid');
    })
  }

  if (typeof contentInput.val() !== "undefined") {
    setContent(contentInput.val());
    contentInput.keyup(function(){
        var newContent = $(this).val();
        setContent(newContent);
    })
  }

  // dynamic title

  var titleInput = $("#id_title");

  function setTitle(value){
    $("#preview-title").text(value);
  }

  if (typeof titleInput.val() !== "undefined") {
    setTitle(titleInput.val());
    titleInput.keyup(function(){
      var newTitle = $(this).val();
      setTitle(newTitle);
    })
  }
  
})