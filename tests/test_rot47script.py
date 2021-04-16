import os
import tempfile
import unittest
import rot47script
from io import StringIO



class TestRot47Script(unittest.TestCase):

    def testencode(self):
        text = rot47script.encode('Welcome to ROT47 Cipher Code!')
        text2 = rot47script.encode('Better done than perfect!')
        text3 = rot47script.encode("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam quis nulla at velit fermentum ullamcorper id sit amet nulla. Mauris ac arcu felis. In hac habitasse platea dictumst. Morbi laoreet orci erat, quis accumsan mauris imperdiet vel. Praesent luctus consequat leo ut hendrerit. Aenean a venenatis nisi. Donec vel ante arcu. Suspendisse sagittis, nibh a scelerisque varius, enim nunc egestas arcu, sit amet placerat leo risus at metus. Integer imperdiet volutpat elit non facilisis. Donec pharetra sapien nunc, non malesuada nunc facilisis id. In eu rhoncus eros. Aliquam vitae enim vitae nulla faucibus mollis. Vivamus ac bibendum dolor, vitae porta mauris.hhDonec tincidunt leo urna, ac ultricies leo efficitur eu. Nam malesuada lectus ac nunc sollicitudin pharetra. In ac tellus tincidunt, condimentum neque eu, interdum eros. Nullam est nulla, iaculis sed magna sed, tempus convallis sem. Maecenas sodales tristique imperdiet. Aenean lectus elit, sagittis in est in, bibendum pellentesque leo. Fusce dignissim pretium nunc, eu aliquam libero. Sed aliquam, quam sit amet bibendum iaculis, sapien quam condimentum ligula, vel ultricies ex mauris id est.hhNullam molestie nisi magna, non sodales est ultrices quis. Aenean gravida est ligula, vestibulum suscipit magna interdum id. Pellentesque magna nibh, placerat quis nibh vehicula, tincidunt efficitur ipsum. Nulla viverra volutpat nulla ac ullamcorper. Duis purus nulla, cursus a blandit at, bibendum quis lectus. Fusce sit amet nisl dui. Ut a magna tincidunt, posuere risus molestie, faucibus nisi. Morbi eu purus nulla. Fusce nec mi quis quam tincidunt egestas ac eget urna. Suspendisse eu pulvinar nisi, eget rhoncus enim. Mauris eget sapien ultricies, hendrerit ligula quis, pharetra leo. Curabitur pretium tortor nec elit ullamcorper sollicitudin. Pellentesque finibus interdum varius. Phasellus sagittis mattis ligula, nec faucibus augue dignissim sed.hhAliquam dignissim feugiat hendrerit. Phasellus commodo gravida posuere. Etiam pellentesque neque in mi vulputate, sit amet blandit risus dictum. Cras venenatis nulla sapien, convallis volutpat elit elementum ac. Praesent vitae lectus pharetra, tincidunt mauris sed, rutrum sapien. Vestibulum aliquet ultricies felis, quis venenatis nibh. Proin tellus risus, ultricies eu metus vel, malesuada tempus lectus. Curabitur mi ligula, pulvinar consectetur vestibulum sed, volutpat eu lacus. Etiam sed massa ultricies, rhoncus est non, volutpat nibh. Aliquam posuere dolor id diam consectetur laoreet. Vivamus felis erat, ornare eu gravida vitae, efficitur ut nisl. Sed facilisis venenatis erat, at scelerisque nunc ullamcorper vel. Vivamus malesuada odio ac cursus cursus. Duis blandit aliquam augue, et consequat nisl aliquet a. Maecenas finibus magna vel ex auctor, vitae congue turpis aliquam. Quisque quis nisi ac elit luctus faucibus a id odio. h""")

        self.assertEqual(text, '(6=4@>6OE@O#~%cfOr:A96COr@56P')
        self.assertEqual(text2,'q6EE6CO5@?6OE92?OA6C764EP')
        self.assertEqual(text3, """{@C6>O:ADF>O5@=@COD:EO2>6E[O4@?D64E6EFCO25:A:D4:?8O6=:E]Op=:BF2>OBF:DO?F==2O2EOG6=:EO76C>6?EF>OF==2>4@CA6CO:5OD:EO2>6EO?F==2]O|2FC:DO24O2C4FO76=:D]Ox?O924O923:E2DD6OA=2E62O5:4EF>DE]O|@C3:O=2@C66EO@C4:O6C2E[OBF:DO244F>D2?O>2FC:DO:>A6C5:6EOG6=]O!C26D6?EO=F4EFDO4@?D6BF2EO=6@OFEO96?5C6C:E]Op6?62?O2OG6?6?2E:DO?:D:]Os@?64OG6=O2?E6O2C4F]O$FDA6?5:DD6OD28:EE:D[O?:39O2OD46=6C:DBF6OG2C:FD[O6?:>O?F?4O686DE2DO2C4F[OD:EO2>6EOA=246C2EO=6@OC:DFDO2EO>6EFD]Ox?E686CO:>A6C5:6EOG@=FEA2EO6=:EO?@?O724:=:D:D]Os@?64OA92C6EC2OD2A:6?O?F?4[O?@?O>2=6DF252O?F?4O724:=:D:DO:5]Ox?O6FOC9@?4FDO6C@D]Op=:BF2>OG:E26O6?:>OG:E26O?F==2O72F4:3FDO>@==:D]O':G2>FDO24O3:36?5F>O5@=@C[OG:E26OA@CE2O>2FC:D]99s@?64OE:?4:5F?EO=6@OFC?2[O24OF=EC:4:6DO=6@O677:4:EFCO6F]O}2>O>2=6DF252O=64EFDO24O?F?4OD@==:4:EF5:?OA92C6EC2]Ox?O24OE6==FDOE:?4:5F?E[O4@?5:>6?EF>O?6BF6O6F[O:?E6C5F>O6C@D]O}F==2>O6DEO?F==2[O:24F=:DOD65O>28?2OD65[OE6>AFDO4@?G2==:DOD6>]O|2646?2DOD@52=6DOEC:DE:BF6O:>A6C5:6E]Op6?62?O=64EFDO6=:E[OD28:EE:DO:?O6DEO:?[O3:36?5F>OA6==6?E6DBF6O=6@]OuFD46O5:8?:DD:>OAC6E:F>O?F?4[O6FO2=:BF2>O=:36C@]O$65O2=:BF2>[OBF2>OD:EO2>6EO3:36?5F>O:24F=:D[OD2A:6?OBF2>O4@?5:>6?EF>O=:8F=2[OG6=OF=EC:4:6DO6IO>2FC:DO:5O6DE]99}F==2>O>@=6DE:6O?:D:O>28?2[O?@?OD@52=6DO6DEOF=EC:46DOBF:D]Op6?62?O8C2G:52O6DEO=:8F=2[OG6DE:3F=F>ODFD4:A:EO>28?2O:?E6C5F>O:5]O!6==6?E6DBF6O>28?2O?:39[OA=246C2EOBF:DO?:39OG69:4F=2[OE:?4:5F?EO677:4:EFCO:ADF>]O}F==2OG:G6CC2OG@=FEA2EO?F==2O24OF==2>4@CA6C]OsF:DOAFCFDO?F==2[O4FCDFDO2O3=2?5:EO2E[O3:36?5F>OBF:DO=64EFD]OuFD46OD:EO2>6EO?:D=O5F:]O&EO2O>28?2OE:?4:5F?E[OA@DF6C6OC:DFDO>@=6DE:6[O72F4:3FDO?:D:]O|@C3:O6FOAFCFDO?F==2]OuFD46O?64O>:OBF:DOBF2>OE:?4:5F?EO686DE2DO24O686EOFC?2]O$FDA6?5:DD6O6FOAF=G:?2CO?:D:[O686EOC9@?4FDO6?:>]O|2FC:DO686EOD2A:6?OF=EC:4:6D[O96?5C6C:EO=:8F=2OBF:D[OA92C6EC2O=6@]OrFC23:EFCOAC6E:F>OE@CE@CO?64O6=:EOF==2>4@CA6COD@==:4:EF5:?]O!6==6?E6DBF6O7:?:3FDO:?E6C5F>OG2C:FD]O!92D6==FDOD28:EE:DO>2EE:DO=:8F=2[O?64O72F4:3FDO2F8F6O5:8?:DD:>OD65]99p=:BF2>O5:8?:DD:>O76F8:2EO96?5C6C:E]O!92D6==FDO4@>>@5@O8C2G:52OA@DF6C6]OtE:2>OA6==6?E6DBF6O?6BF6O:?O>:OGF=AFE2E6[OD:EO2>6EO3=2?5:EOC:DFDO5:4EF>]OrC2DOG6?6?2E:DO?F==2OD2A:6?[O4@?G2==:DOG@=FEA2EO6=:EO6=6>6?EF>O24]O!C26D6?EOG:E26O=64EFDOA92C6EC2[OE:?4:5F?EO>2FC:DOD65[OCFECF>OD2A:6?]O'6DE:3F=F>O2=:BF6EOF=EC:4:6DO76=:D[OBF:DOG6?6?2E:DO?:39]O!C@:?OE6==FDOC:DFD[OF=EC:4:6DO6FO>6EFDOG6=[O>2=6DF252OE6>AFDO=64EFD]OrFC23:EFCO>:O=:8F=2[OAF=G:?2CO4@?D64E6EFCOG6DE:3F=F>OD65[OG@=FEA2EO6FO=24FD]OtE:2>OD65O>2DD2OF=EC:4:6D[OC9@?4FDO6DEO?@?[OG@=FEA2EO?:39]Op=:BF2>OA@DF6C6O5@=@CO:5O5:2>O4@?D64E6EFCO=2@C66E]O':G2>FDO76=:DO6C2E[O@C?2C6O6FO8C2G:52OG:E26[O677:4:EFCOFEO?:D=]O$65O724:=:D:DOG6?6?2E:DO6C2E[O2EOD46=6C:DBF6O?F?4OF==2>4@CA6COG6=]O':G2>FDO>2=6DF252O@5:@O24O4FCDFDO4FCDFD]OsF:DO3=2?5:EO2=:BF2>O2F8F6[O6EO4@?D6BF2EO?:D=O2=:BF6EO2]O|2646?2DO7:?:3FDO>28?2OG6=O6IO2F4E@C[OG:E26O4@?8F6OEFCA:DO2=:BF2>]O"F:DBF6OBF:DO?:D:O24O6=:EO=F4EFDO72F4:3FDO2O:5O@5:@]O9""")


    def testdecode(self):
        text = rot47script.decode("""}:6OH:6>O;2<2O3C@?O365K:6OFKJH2?2OA@54K2DO%CK64:6;O(@;?JO$H:2E@H6;[O2=6O>JD=6[O+6OrKH2CE2O365K:6O?2O<:;6O:O<2>:6?:6""")
        text2 = rot47script.decode("(J@3C2K?:2O;6DEOH2K?:6;DK2O@5OH:65KJ]O]]]O")
        text3 = rot47script.decode("""}:6O;6DE6>ODK4K68@=?:6OFE2=6?E@H2?J]O|@;2OA2D;2O;6DEOA@OAC@DEFO4:6<2H@D4]""")

        self.assertEqual(text, """Nie wiem jaka bron bedzie uzywana podczas Trzeciej Wojny Swiatowej, ale mysle, Ze Czwarta bedzie na kije i kamienie""")
        self.assertEqual(text2, "Wyobraznia jest wazniejsza od wiedzy. ... ")
        self.assertEqual(text3, 'Nie jestem szczegolnie utalentowany. Moja pasja jest po prostu ciekawosc.')


    def test_file_open(self):
        file_name = 'text1'
        with open(file_name, 'r') as f:
            new_file = f.read()
        test_f = rot47script.file_open(file_name)
        self.assertEqual(test_f, new_file)


    def test_savefile(self):
        file_name = 'text_0'
        text = 'I really do not know that type here'
        with open(file_name, 'r') as f:
            new_file = f.read()
        test_f = rot47script.save_file(file_name,text)
        self.assertEqual(test_f, new_file)

if __name__ == '__main__':
    unittest.main()

# encode
# decode
# save_file
# file_open
