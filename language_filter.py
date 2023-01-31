import re
class text_filter:


    def phone_filter(self, text):

        phoneregex = re.compile(r'''(
        (\(\d{1,3}\) | \d{1,3})
        (\.|-|s)? 
        (\d{3}) 
        (\.|-|s)? 
        (\d{4})
        (\.|-|s)?
        (\d{,3})?
        )''', re.VERBOSE) #REVORBESE IS FOR Seperating logical expression, we can read clearly when we seperate.

        PhonesTuple = phoneregex.findall(text)

        Phones = []

        for x in PhonesTuple:
            for y in x:
                if(len(y) >= 10):
                    Phones.append(y)
        print(Phones)

    def email_filter(self, text):
        emailregex = re.compile(r'''(
            [a-zA-Z0-9._%+-]+
            @
            [a-zA-Z0-9.-]+
            (\.[a-zA-Z]{2,4})
        )''', re.VERBOSE)

        MailsTuple = emailregex.findall(text)
        Mails = []

        for i in MailsTuple:
            for j in i:
                if (len(j) >= 6):
                    Mails.append(j)

        print(Mails)

    def website_filter(self, text):
        websiteregex = re.compile(r'''(
        (https:// | http://)?
        (www\.)
        [a-z0-9-]+
        \.
        [a-z]{1,15}
        )''', re.VERBOSE)

        #\.
        #[a-z]+

        websiteTuple = websiteregex.findall(text)
        Websites = []

        for i in websiteTuple:
            for j in i:
                if (len(j) >= 9):
                    Websites.append(j)

        print(Websites)


if __name__ == "__main__":
    text_for_phone1 = "ABC +905339742674 ABC 05339742674 ABC (90)5339742674 ABC +90-533-974-2674 4ABC 533-974-2674 ABC 5369740674ABC123123123"
    text1 = text_filter()
    text1.phone_filter(text_for_phone1)

    text_for_email1 = "alper@gmail.com,alper@outlook.com, 123a@hotmail.com asdas131@gmail.com3121"
    text2 = text_filter()
    text2.email_filter(text_for_email1)

    text_for_website = "https://www.alper.com a,21http://www.alper.com, htpww.com www.alper.com , asdasx ww.com htp.123a"
    text3 = text_filter()
    text3.website_filter(text_for_website)






