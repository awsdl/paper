package com.utils.util;

import com.utils.util.HammingUtils;
import com.utils.util.SimHashUtils;
import com.utils.util.TxtIOUtils;


public class test {
    public static void main(String[] args) {
        String[] str = new String[6];
        str[0] = TxtIOUtils.readTxt("D:/test/orig.txt");
        str[1] = TxtIOUtils.readTxt("D:/test/orig_0.8_add.txt");
        str[2] = TxtIOUtils.readTxt("D:/test/orig_0.8_del.txt");
        str[3] = TxtIOUtils.readTxt("D:/test/orig_0.8_dis_1.txt");
        str[4] = TxtIOUtils.readTxt("D:/test/orig_0.8_dis_10.txt");
        str[5] = TxtIOUtils.readTxt("D:/test/orig_0.8_dis_15.txt");
        String ansFileName = "D:/test/ansAll.txt";
        for(int i = 0; i <= 5; i++){
            double ans = HammingUtils.getSimilarity(SimHashUtils.getSimHash(str[0]), SimHashUtils.getSimHash(str[i]));
            TxtIOUtils.writeTxt(ans, ansFileName);
        }


    }
}
