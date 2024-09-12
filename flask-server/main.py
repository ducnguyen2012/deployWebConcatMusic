
from conCatFile import conCatFile
import os

# g = getSongFromDrive()
# g.setURL("https://drive.google.com/drive/folders/1wCGmMup3hHBE8O9R8Ifn-7CTAqRMDJUV?fbclid=IwY2xjawEdwLpleHRuA2FlbQIxMAABHbsX2grkpgeEiw61U9MQHTh7rn92aHZfsS109dLt1vO-9TQZtNEL8H_elw_aem_X0-sCY47hm8TR-g2RQW2ew")
# g.getSong()

concat = conCatFile(os.getcwd() + "\\uploads\\")
res = concat.conCatFileMP3()
print(res)