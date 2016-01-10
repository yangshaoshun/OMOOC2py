<!DOCTYPE html>
<html>
<head>
   <title>Bootstrap 实例 - 基本表单</title>
   <link rel="stylesheet" href="http://apps.bdimg.com/libs/bootstrap/3.3.0/css/bootstrap.min.css">
   <script src="http://apps.bdimg.com/libs/jquery/2.1.1/jquery.min.js"></script>
   <script src="http://apps.bdimg.com/libs/bootstrap/3.3.0/js/bootstrap.min.js"></script>
</head>
<body>
<form action="/text" method="post">
<form role="form">
   <div class="form-group">
      <label for="name">请输入日记</label>
      <input type="text" class="form-control" name="indata" 
         placeholder="请输入名称">
   </div>

<form role="form">
  <div class="form-group">
    <label for="name">历史记录</label>
    <textarea class="form-control" rows="20">
    %for row in history:
          %for col in row:
              {{col}}
          %end
    %end
    </textarea>
  </div>
</form>

</body>
</html>	
