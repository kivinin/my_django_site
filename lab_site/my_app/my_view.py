from django.http import HttpResponse
def post_list(request):
 html = "<HTML>
<HEAD>
    <TITLE>Формы</TITLE>
</HEAD>
<BASE>

<BODY bgcolor=”silver”>
    <FORM>
        <CENTER>
            <FONT size=6>Элементы диалога</font>
        </center>
        <HR color=”blue”>
        <Н2>Элемент ISINDEX</h2>
            <ISINDEX prompt=”Cтpoкa для ввода критерия поиска”>
            <HR color=”blue”>
            <Н2>Элементы INPUT</h2>
                <H3> Ввод текстовой строки </h3>
                <INPUT type=”text” size=50>
                <H3> Ввод пароля </h3>
                <INPUT type=”password”>
                <H3> Флажки </h3>
                <INPUT type=”checkbox” name=”F001″ checked>
                <INPUT type=”checkbox” name=”F001″ checked>
                <H3> Переключатели </h3>
                <INPUT type=”radio” name=”S001″ vаluе=”Первый”>
                <INPUT type=”radio” name=”S001″ value=”Второй”>
                <INPUT type=”radio” name=”S001″ value=”Третий” checked>
                <H3> Кнопка подтверждения ввода </h3>
                <INPUT type=”submit” value=”Подтверждение”>
                <H3> Кнопка с изображением </h3>
                <INPUT type=”image” src=”lycos.gif”>
                <H3> Кнопка очистки формы </h3>
                <INPUT type=”reset” value=”0чистка”>
                <H3> Файл </h3>
                <INPUT type=”file” name=”photo” accept=”image/*”>
                <HR color=”blue”>
                <Н2>Элемент SELECT
                    <SELECT multiple>
                        <OPTION value=а>Первый
                            <OPTION value=Ь>Второй
                                <OPTION value=с>Третий
                                    <OPTION value=d>Четвертый
                    </select>
                    </h2>
                    <HR color=”blue”>
                    <Н2>Элемент TEXTAREA
                        <TEXTAREA rows=5 cols=30>
                            Область для ввода текста
                        </textarea>
                        </h2>
                        <HR color=”blue”>
    </FORM>
</BODY>

</HTML>"
 return HttpResponse(html)
