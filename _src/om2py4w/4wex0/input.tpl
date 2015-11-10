<form action="/text" method="post">
        </p>请输入单行日记:
        <input type="text" name="indata" />
        <input type="submit" value="确认" /></p>
%with open("mydaily.log") as history:
    %for line in history:
        <p>{{line,}}</p>  
    %end
</form>