# netflixSeleniumTest
can login netflix automatically and test some features with screenshots and give pass/fail feedback via txt

<br>

<b>Selenium ile Netflix Testi</b>
<br>
<p>Uygulana selenium webdriver sayesinde otomatik olarak netflix sayfasını açar, login sayfasına gider.
<br>
  UserInfo.py dosyasında belirttiğiniz kullanıcı bilgilerinizi otomatik olarak giriş yapmak için kullanır.
</p>
Önerilen filmi seçer, bir süre izler, ileri sarma işlevini test eder. geri sarma işlevini test eder.
</p>
XPath yoluyla ulaştığı bu işlevleri test etmesinin yanı sıra her işlev kontrolünden sonra PASS/FAIL bilgisini size verir/konsola yazdırır.
<br>
Bir işlevde FAIL durumu olursa diğer işlevlerin kontrolüne devam etmez.
<br>
Yaptığı her işlemden sonra ilgili sayfaya ait screenshot alır ve saklar.
<br>
Program bitişinde konsola yazdırdığı PASS/FAIL durumlarını txt oluşturup içerisinde bir rapor olarak saklar.

 <h2>Kullanım</h2>
<p> Selenium WebDriver kurulumu/path(*) gerçekleştirin. </p>
<p> UserInfo bilgilerini kendi bilgilerinizle güncelleyin. </p>
</br>
