# Judging packets: fixed Hinglish-output summaries (25 windows, 100 summaries)

How to use:
1. Open a NEW chat with Claude Sonnet 5.5 (the same judge as before).
2. Paste the INSTRUCTIONS block as the first message.
3. Paste ONE window block per message (25 messages). Start a fresh chat after about 8 windows (paste the INSTRUCTIONS again each time).
4. Copy all reply lines (like `G-W03-2: 1010011001`) into one text file and send it back.

Most summaries are in Hindi (Devanagari) or Hinglish. Judge them exactly the same way: a fact counts in any language or script. A summary that degenerates into repeated words only gets credit for facts it actually stated before that.

## INSTRUCTIONS (paste first)

```
You are a strict, consistent evaluator of summary content.

Decide, for each numbered fact, whether the SUMMARY conveys it.

A fact is supported if the summary states its core information or clearly implies it, even in different words, in another language (English, Hindi or Hinglish) or in another script. It is not supported if it is missing, only vaguely related, or contradicted. Judge each fact independently, using only the summary.

Additional rules (apply identically to every summary):
1. Facts whose core is a specific path, shortcut, value or name (e.g. "File > Save", "Ctrl+Alt+T", "gcc ... -o args", "right to top", "228") need that specific element; a generic mention ("saves the file") does not count.
2. A contradicted fact (wrong value/direction) is unsupported.
3. A garbled product name does not by itself cancel a correctly stated fact.
4. Hallucinated content never supports a fact.

For each SUMMARY id I send, reply with exactly one line: <id>: <bit string>, one digit per fact in order (1 = supported, 0 = not supported). No other text.
```

## Window W00 (10 facts, 4 summaries)

```
FACTS:
1. A shortcut for Mozilla Thunderbird can be added by dragging its icon onto the launcher.
2. Unread emails in the inbox are indicated by bold text.
3. New emails are retrieved by clicking the Get Mail icon and choosing get all new messages.
4. Clicking the From column heading arranges the messages in alphabetical order.
5. Clicking the Subject heading sorts the inbox messages by subject.
6. Tagging an email as important displays that message in red.
7. Clicking the tagged icon in the Quick Filter toolbar filters the view to show only tagged messages.
8. Related messages shown in sequence or as a conversation are defined as message threads.
9. Clicking the threading symbol next to a thread reveals the complete conversation.
10. Clicking the thread icon again exits the thread view.

SUMMARY G-W00-1:
<<<
This tutorial explains how to use Thunderbird on Ubuntu 12.04, focusing on creating a Thunderbird shortcut in the launcher, tagging messages, sorting them by various criteria like sender or subject, and organizing them into threads. It covers adding Thunderbird to the launcher by dragging its icon from the Dash to the Launcher. The tutorial also demonstrates how to mark messages as important, use quick filters to view tagged messages, and manage message threads for continuous conversations. Additionally, it shows how to save and print messages by creating a folder named "Saved Mails" on the desktop.
>>>

SUMMARY G-W00-2:
<<<
इस टिटोरियल में हमने थंडरबर्ड का उपयोग कैसे करना सीखा। लॉन्चर में थंडरबर्ड शॉर्टकट जोड़ना, मैसेज टैग करना, तीव्र बदलाव करना, और मैसेज श्रेणीबद्ध करना सीखा। थंडरबर्ड शॉर्टकट लॉन्चर पर ड्रैग और ड्रॉप करके जोड़ा जा सकता है। मैसेज श्रेणीबद्ध करने के लिए फॉर्मेट चुनिंग करें, जैसे फ्रॉम, ऑब्जेक्ट, डेटा रिसेव आदि। मैसेज इकट्ठा करने के लिए टैग उपयोग कर सकते हैं। उपयोगकर्ता द्वारा टैग किए गए मैसेज देखने के लिए क्विक फिल्टर टूलबार का उपयोग कर सकते हैं। मैसेज थ्रेड्स देखने के लिए थ्रेडिंग आइकॉन बाईं कोने पर क्लिक करें। मैसेज बनाने के लिए नया फोल्डर बनाकर मैसेज बनाए और फिर प्रिंट कर सकते हैं।
>>>

SUMMARY G-W00-3:
<<<
Thunderbird का उपयोग करने का ट्यूटोरियल में हम शॉर्टकट आइकन जोड़ने, मैसेज टैग करने, तीव्र बदलाव करने और मैसेज श्रेणीबद्ध करने की विधि सीखते हैं। शॉर्टकट आइकन जोड़ने के लिए, दश घोषणा पर क्लिक करें, फिर तार्किक क्षेत्र में Thunderbird टाइप करें और आइकन लैंचर पर ड्रैग और ड्रॉप करें। मैसेज श्रेणीबद्ध करने के लिए, फ्रॉम या विषय द्वारा क्लिक करें। मैसेज टैग करने के लिए, इनबॉक्स में मेसेज चुनें और टूलबार में टैग आइकन पर क्लिक करें। मैसेज फोल्डर में सेव और प्रिंट करने के लिए, नए फोल्डर बनाएं और सेव किए गए मैसेज इसमें रखें।
>>>

SUMMARY G-W00-4:
<<<
इस पोकेट टीटूरल में हमने तन्रबद शोट कैसे लेने और लाँचर में जोड़ने की जानकारी दी है। तन्रबद शोट लेने के लिए, डश होंपर क्लिक करें, फिर सर्च फिल्ड में तन्रबद लिखें, तन्रबद आएका दिखाई देता है, इसे चुनें और बाय माउस बटन दबाएं। फिर लाँचर पर दबाएं और बाय माउस बटन खोलें। तन्रबद विन्डो खुलेगा और गेम लॉगिन करें। इंबोक्स पर क्लिक करें और देखें कि किन मेसेज़े बोल्ड हैं। गेट मेल पर क्लिक करें और फ्रुम पर क्लिक करें। यह मेसेजेज़ श्वेनी बद होंगे। फिर सबज्ट पर क्लिक करें और नानु क्रमी क्रम में श्वेनी बद करें। इस तरह से आप आसानी से मेसेजेज़ श्वेनी बद कर सकते हैं। आप भी मेसेजेज़ तैक कर सकते हैं और फिर से खुलने के लिए उप्यो कर सकते हैं। आप एक साथ इकठा करने के लिए भी तैक्स का उप्यो कर सकते हैं। आप एक मेल को मेट पुर के रूप में तैक कर सकते हैं और इन वोक्स पर ख्लिक करें। फिर सेव और प्रिंट मैसेजेज़ नामक फुल्टर बनाएं।
>>>

Reply with 4 lines, each with exactly 10 digits.
```

## Window W01 (10 facts, 4 summaries)

```
FACTS:
1. A slide background refers to all colors and effects applied behind the content of the slide.
2. Any alteration made to the master slide applies to every slide in the presentation.
3. The Slide Master view is opened by navigating to View, selecting Master, and clicking Slide Master from the main menu.
4. The master view toolbar can be used to create, delete, and rename master pages.
5. A white background can be applied by choosing the blank option under bitmap fill in the Page Setup dialog box.
6. The text color can be set to black from the Font Effects tab within the Character dialog box.
7. A light blue color can be applied to a slide by selecting Blue 8 from the color fill dropdown menu in Page Setup.
8. The basic shapes toolbar at the bottom of the screen allows users to draw various basic shapes.
9. When drawing a rectangle, the cursor displays a plus sign accompanied by a capital letter I.
10. The control points that appear on a selected object are eight small blue squares used to resize it.

SUMMARY G-W01-1:
<<<
लिबर अफिस इंप्रस पर श्लाइद मास्टर और श्लाइद दिशाइन बनाने की टीटौरल में, आप अपने बैग्रून को सभी स्लाइट्स में लागू कर सकते हैं। इसके लिए आप अस्लाइट मास्टर अप्षन का इस्तिमाल कर सकते हैं। आप नए बैग्रून को लागू करने के लिए मास्टर चुनकर फोरमेटिंग प्रफिंषेज का इस्तिमाल कर सकते हैं। उदाहरण के लिए, आप सफेद बैग्रून लगाने के लिए फोरमेटिंग प्रफिंषेज का इस्तिमाल कर सकते हैं। आप टेक्स्ट के रंग को भी बदल सकते हैं और आयत आकार बनाने के लिए बेसिक शिप्स तूलबार का इस्तिमाल कर सकते हैं। आप नीले रंग के आयत बनाने के लिए बेसिक शिप्स तूलबार का इस्तिमाल कर सकते हैं। आप नीचे लोगो या आकार जोड़ सकते हैं और उन्हें निर्दिष्ट स्थान पर रख सकते हैं।
>>>

SUMMARY G-W01-2:
<<<
This tutorial explains how to apply backgrounds and designs to slides using LibreOffice Impress on a GNU/Linux operating system. It covers customizing slide masters and applying them across all slides. To change the background, you select the Slide Master, then choose the desired background from the Format menu. For a white background, you set the fill to bitmap and choose blank. Changing text color to black improves readability against a white background. Adding colors or shapes involves selecting the appropriate options from the context menu or toolbar. The tutorial also demonstrates adding elements like logos and shapes, such as rectangles, to slides. Overall, it guides users through creating visually appealing presentations with customized backgrounds and designs.
>>>

SUMMARY G-W01-3:
<<<
लिबर ऑफिस impress में slide के लिए background और डिजाइन लागू करने की विधि सीखेंगे। आप अपने गनु लिनक्स और लिबर ऑफिस 334 का उपयोग कर सकते हैं। फर्स्ट, आपको sampleimpress odp प्रस्तुति खोलना है। फिर custom background बनाने के लिए slide master चुनें। आपको अपने प्रस्तुति के सभी slides के लिए एक सामान्य background लगाना है। फर्स्ट, आपको main menu से view पर क्लिक करना है और फिर slide master पर। यहाँ master slide प्रदर्शित होगी। आप यहाँ master pages तैयार कर सकते हैं। फिर आपको पहले slide चुनना है और फिर फैर्मेट पर क्लिक करके पेज सेटअप डायलॉग बॉक्स खोलना है। यहाँ आप background टैब पर क्लिक करके फिल्ड डाउनलोड में बिट맵 ऑप्शन चुन सकते हैं। फिर आप ब्लांक ऑप्शन चुनकर ऑक क्लिक कर सकते हैं। अब आपके slide में सफेद background होगा। आप अपने text का रंग भी बदल सकते हैं। फिर आप अपने text को चुनकर फैर्मेट पर क्लिक करके चरक्टर चुन सकते हैं। यहाँ आप फैनट फैक्टिब्स टैब पर क्लिक करके फैनट लाइन डाउनलोड में ब्लैक ऑप्शन चुन सकते हैं। फिर ऑक क्लिक करें। अब आप अपने रंग को slide पर लागू कर सकते हैं। फिर आप कंटेक्स्ट मेनू के लिए slide पर राइट क्लिक करके slide और पेज सेटअप पर क्लिक कर सकते हैं। यहाँ आप फिल्ड डाउनलोड में कॉलर ऑप्शन चुनकर लाल रंग लगा सकते हैं। फिर ऑक क्लिक करें। आप अपने प्रस्तुति में लॉगो जोड़ सकते हैं। आप बेसिक शेफ्स टैब से वृत्त या आयत बना सकते हैं। फिर आप उस आयत
>>>

SUMMARY G-W01-4:
<<<
लिबर ऑफिस इम्प्रेस में स्लाइड मेस्टर और डिजाइन सीखेंगे। आपको बताया गया कि बैकग्राउंड और डिजाइन इम्प्रेस में लागू कैसे करें। आप अपने गनु लिनक्स ऑपरेटिंग सिस्टम और लिबर ऑफिस वर्सन 3.3.4 का उपयोग करेंगे। बैकग्राउंड लागू करने के लिए स्लाइड मेस्टर विक्स चुनें। बैकग्राउंड बदलने के लिए स्लाइड मेस्टर पर जाकर बैकग्राउंड टैब पर क्लिक करें और बिटमैप ऑप्शन चुनें। फिर ब्लैंक चुनें और ऑक करें। आप भी अपने आयत बना सकते हैं और इसके आकार को समायोजित कर सकते हैं। लोगो जोड़ने के लिए बेसिक शेप्स टैब पर जाकर आयत बनाएं और इसे टाइटल क्षेत्र में रखें। इससे आप अपनी प्रस्तुति को आकर्षक बना सकते हैं।
>>>

Reply with 4 lines, each with exactly 10 digits.
```

## Window W02 (11 facts, 4 summaries)

```
FACTS:
1. Gedit text editor comes pre-installed in the Ubuntu Linux operating system.
2. Gedit can be launched by searching for gedit in Dash Home and clicking the text editor icon.
3. Gedit can also be launched via the terminal by pressing Ctrl + Alt + T, typing gedit, and pressing Enter.
4. The default tab name assigned to a new document in gedit is Untitled Document 1.
5. An asterisk displayed next to a file name in the tab indicates that the file has not been saved.
6. The status bar displays the cursor position in terms of line number and column number.
7. The default text mode in gedit is insert mode, indicated as ins.
8. To save a file, click the File option in the menu bar and select Save.
9. To close an open file, click File in the menu bar and choose Close.
10. A new file can be created by clicking the plus sign icon on the toolbar.
11. An existing document can be opened by clicking File in the menu bar and selecting Open.

SUMMARY G-W02-1:
<<<
इस टूटोरियल में हम जी एडिट टेक्स्ट एडिटर को संस्थापित करने और इसका इस्तेमाल करने के बारे में सीखते हैं। पहले हम जी एडिट टेक्स्ट एडिटर को विंडोज और लिनुक्स में संस्थापित करते हैं। फिर नया फाइल बनाने, फाइल खोलने, सेवने और बंद करने की विधियाँ सीखते हैं। टेक्स्ट एडिटर में डॉक्यूमेंट टैब, मेन्यू बार, फाइल सेवने और बंद करने के लिए विभिन्न विकल्प दिखाई देते हैं। फाइल सेवने के लिए मेन्यू बार में फाइल ऑप्शन और सेव चुनें। फाइल बंद करने के लिए मेन्यू बार में पर चुनें। फाइल खोलने के लिए फाइल में चुनें और ओपन बटन पर क्लिक करें। यह टूटोरियल आपको जी एडिट टेक्स्ट एडिटर का इस्तेमाल करने में मदद करेगा।
>>>

SUMMARY G-W02-2:
<<<
This tutorial introduces the gedit text editor for Ubuntu Linux and Windows systems. It covers how to install gedit on Ubuntu Linux using the Ubuntu Software Centre or by opening it from the Dash Home. On Windows, instructions for installation are provided via a link. The tutorial explains how to create a new file, open an existing one, and save changes. It also demonstrates closing files and opening them again. Key features like the menu bar, toolbars, and status bar are introduced. The tutorial shows how to switch between overwrite and insert modes, save files with names, and handle unsaved changes. It emphasizes the importance of saving files regularly to prevent data loss due to power cuts or system crashes.
>>>

SUMMARY G-W02-3:
<<<
इस ट्यूटोरियल में हम जी अटिट टेक्स अटिटर को सापित करने और फायल को खोलने, खुलाने, और सेव करने की शिक्षा मिलेगी। पहले हम बिन्दोस पर जाकर जीएडिट टेक्स अटिटर को संस्थापित करेंगे। उबंटू लिनेक्स में यह पहले से ही होता है। फिर जी अटिट टेक्स अटिटर खोलकर एक नया फायल बनाएंगे। फायल में कार्य करने के लिए तर्मिनल खोलकर भी जी अटिट टेक्स अटिटर खोल सकते हैं। फायल को सेव करने के लिए पाल अपशन पर क्लिक करें और फिर सेप डालोग बोक्स खोलें। फायल को खोलने के लिए इस्ट्रिक अपशन पर क्लिक करें। यह टेक्स अटिटर में कार्य करने के लिए बहुत मदददाता है।
>>>

SUMMARY G-W02-4:
<<<
इस ट्यूटोरियल में हम गेडिट टेक्स्ट एडिटर को संस्थापित करने और इसका इस्तेमाल करने के बारे में सीखते हैं। गेडिट ऊबंटु लिनक्स और विंडोज में उपलब्ध है। इसको संस्थापित करने के लिए उबंटु सॉफ्टवेयर सेंटर या टर्मिनल का उपयोग कर सकते हैं। गेडिट खोलने के लिए डेश होम पर क्लिक करें या टर्मिनल में `gedit` लिखें। गेडिट खोलने के बाद, टैब देख सकते हैं जो नए डाक्ट्रम का नाम दिखाता है। गेडिट में टाइपिंग करने के लिए टाइप क्षेत्र देख सकते हैं। फाइल को सेव करने के लिए, मेनुबार में फाइल चुनें और सेव चुनें। फाइल को बंद करने के लिए, मेनुबार में फाइल चुनें और बंद चुनें। फाइल को खोलने के लिए, मेनुबार में फाइल चुनें और खोलें चुनें।
>>>

Reply with 4 lines, each with exactly 11 digits.
```

## Window W03 (11 facts, 4 summaries)

```
FACTS:
1. Snippets are lines of text or source code frequently used while writing programs.
2. Snippets is a default plugin in the gedit text editor.
3. The snippets plugin can be enabled in gedit via Edit, Preferences, checking the snippets box in the plugin tab, and clicking close.
4. Typing "if" and pressing the Tab key automatically inserts the structure of an if statement.
5. When an if statement snippet is inserted, the cursor defaults to the condition word.
6. Auto-closing brackets and quotes is a feature of the intelligent text completion plugin.
7. Selecting Tools and Manage Snippets from the main menu opens the Manage Snippets dialog box.
8. Selecting C and clicking its triangle symbol lists all snippets available for C.
9. The tab trigger for the else if snippet is elif.
10. Typing "elif" and pressing Tab inserts the syntax for an else if statement.
11. Clicking the plus icon at the bottom right of the window allows the user to create a new snippet.

SUMMARY G-W03-1:
<<<
Gedit text editor mein snippets ka use kaise karein, usse create kaise karein aur kaise delete karein, wese bata diye gaye hain. Snippets text ya source code ke lines hain jo typing ko kam karte hain. Gedit mein default snippets plugin hai, usko activate karne ke liye main menu se edit aur preferences par click karo, plugin tab me snippets box check karo. C program likhne ke liye file numcheck.c naam se save karo, tab if statement ke liye cursor next line pe rakhke tab press karo. Intelligent text completion plugin se auto close brackets and quotes milte hain. Manage snippets dialog box se custom snippets add kar sakte hain, usse c ke liye click karo, c snippet list dekh sakte hain. Uske liye tab trigger field dekhne ka use karo. Aap apne program mein custom snippets ka use karke typing ko kam kar sakte hain. Custom snippets create karna ke liye tools aur manage snippets par click karo, c ke liye click karo, plus icon pe click karo, helloworld type karo, enter press karo, edit panel pe click karo aur simple c program type karo.
>>>

SUMMARY G-W03-2:
<<<
This tutorial covers using snippets in the gedit text editor, primarily for programming tasks. Snippets are pre-defined pieces of text or source code that can save time by reducing the need for repetitive typing. To enable snippets in gedit, you must activate the plugin via the Edit > Preferences menu under the Plugins tab. Once enabled, typing `if` followed by Tab inserts an if statement with default conditions and brackets. The intelligent text completion feature automatically closes brackets and quotes. The Manage Snippets dialog allows you to view and customize existing snippets; clicking on a snippet shows its syntax. For creating custom snippets, go to Tools > Manage Snippets, select the language, click the plus icon, and define your snippet's content. This tutorial demonstrates how to use predefined snippets like `if` and `else if`, and how to create a simple "Hello World" snippet for basic C programs.
>>>

SUMMARY G-W03-3:
<<<
इस टुटोरियल में हम डिफॉल्ट स्नीपर्स का उपयोग और नए स्नीपर्स जोड़ने के बारे में सीखते हैं। जी एडिट टेक्स्ट एडिटर में स्नीपर्स का उपयोग करने के लिए पहले स्नीपट प्लगिन को सक्षम करना चाहिए। फिर स्निपट पैनल से स्नीपर्स चुनकर उनका उपयोग कर सकते हैं। उदाहरण के लिए, एक `if` statement का उपयोग करके दोहराव को टाइपिंग से बच सकते हैं। अपने खुद के स्नीपर्स बनाने के लिए, मेन मेनू से टूल्स और मैनेज स्नीपर्स पर क्लिक करें, फिर नए स्नीपर्स को बनाने के लिए प्लस आइकन पर क्लिक करें। इस प्रकार हम स्नीपर्स का उपयोग करके सोर्स कोड में दोहराव टाइपिंग से बच सकते हैं।
>>>

SUMMARY G-W03-4:
<<<
आपको लिनेक्स 14.04 और अदिटर 3.10 का उपयोग करने का टॉटरिल देखने के लिए स्वागत है। आपको पहले इस्मिपट्स प्लगिन्स को सक्षम करना है। इस्मिपट प्लगिन्स को सक्षम करने के लिए लिनेक्स से अदिटर टेक्स और अदिटर 3.10 को खोलें। फिर इस्मिपट प्लगिन्स को नीचे डाउनलोड करें और स्वोक्स चेक करें। इस्मिपट स्वोक्स चेक करें। अगर आप इस्मिपट प्लगिन्स को उप्योप करना चाहते हैं, तो एक सी प्रोग्राम लिखें। पहले पायल को नम्चैक दोट सी नाम सी सेप करें। अब इप श्वाब ताएप की दमाएं लिखें। इसके बाद इप स्टेट्मिन्ट की संदर्भ देखें। इस्नी पेट्स चुनें और अपने करली ब्रैसिस और अन ब्रैसिस देखें। इस्नी पेट्स चुनें और बाई उन पैनल पर निचे इस्क्राल करें। फिर सी चुनें और इसके आगे प्रिज़ा अप्रिकोड के चिन्पर क्लिक करें। इस प्रकार से आप सी के लिए सब विस्मी पर्स की सुची देख सकते हैं। इस प्रकार से आप अपने प्रोग्राम को सिंटेक्स के रूप में देख सकते हैं। अपने इस्मिपट पेट को बनाने के लिए अपने इस्मिपट पेट सपक लिक परीं और अदेक पैनल पर ख्लिख करी निम कोर ताइप करी। यह एक सी मेसरल गुन्यादी पुग्राम है।
>>>

Reply with 4 lines, each with exactly 11 digits.
```

## Window W04 (10 facts, 4 summaries)

```
FACTS:
1. The sampleimpress.odp presentation is opened to begin the tutorial.
2. A text box is selected by clicking on its text and then clicking on the visible border.
3. The entrance tab controls the way an object appears on the screen.
4. The diagonal squares animation is selected under the basic category.
5. The wedge animation under basic animation is chosen with the speed set to medium.
6. Multiple animations can be selected for preview by holding down the Shift key.
7. The order of animations can be modified using the change order buttons.
8. Double-clicking the first animation in the list opens the effects options dialog box.
9. The animation direction can be adjusted to from right to top under settings.
10. An animation delay can be increased in the delay field under the timing tab.

SUMMARY G-W04-1:
<<<
This tutorial covers creating custom animations in LibreOffice Impress, using a GNU Linux operating system and version 334 of the LibreOffice suite. To start, open a presentation file and select a slide. Choose an element on the slide, such as a text box, and then access the Custom Animation feature from the Tasks pane. The Custom Animation dialog box appears, where you can choose the type of animation, such as entrance or motion paths. You can also adjust the speed and order of animations. For example, you can set one animation to move diagonally and another to move in a wedge shape. Animations are added to the list in the order they are created. To change the order, double-click an animation to open the Effect Options dialog box. Here, you can modify properties like direction and delay. By adjusting these settings, you can create more dynamic and engaging presentations.
>>>

SUMMARY G-W04-2:
<<<
इस tutorial में हम लिबर ऑफिस impress में custom animation के बारे में सीखते हैं। पहले हम एक sample प्रस्तुति खोलते हैं और फिर एक टेक्स्ट बॉक्स को चुनते हैं। फिर tasks pane में custom animation पर क्लिक करते हैं और एक custom animation dialog box देखते हैं। यहाँ आप entrance टैब का उपयोग करके वस्तु को दिखाने के तरीके को नियंत्रित कर सकते हैं। आप गति भी नियंत्रित कर सकते हैं। फिर आप एक animation चुनते हैं और play पर क्लिक करते हैं। दूसरे टेक्स्ट बॉक्स को चुनकर और custom animation के नीचे add पर क्लिक करके दूसरा animation जोड़ते हैं। आप एक animation को दोबारा डब्ल्यूक्लिक करके उसके विवरणों को देख सकते हैं। आप timing टैब पर क्लिक करके दिलाई गई देरी को बदल सकते हैं। इस प्रकार आप अपनी प्रस्तुति को अधिक आकर्षक बना सकते हैं।
>>>

SUMMARY G-W04-3:
<<<
इस ट्यूटोरियल में दिए गए अनिमेशन का उपयोग करके प्रस्तुती को आकर्षक बनाने की विधि बताई गई है। पहले टेक्स्ट बॉक्स को चुनें और फिर बोर्ड पर क्लिक करें। इंप्रस्ट विन्डो में बाई योर टास्ट्स पैन में कुस्टम अनिमेशन पर क्लिक करें। अन्ट्रेंस टैब खोलने के लिए अपने गती को निर्णय रखें। बेसिक अनिमेशन में वेज और गती को निर्धारित करें। दुसरे टेक्स्ट बॉक्स को चुनें और अन्ट्रेंस टैब में दागनल चुनें। अनिमेशन के क्रम को बदलने के लिए अप चेंज अडर बटन्स का उपयोग करें। दीफाल्ट प्रपर्टीशेज को देखें और बड़ाउ कैसे करें। अनिमेशन को बन्द करने के लिए वोक बटन पर क्लिक करें। प्ले बटन पर क्लिक करके अनिमेशन देखें और फिर अनिमेशन डालोग बॉक्स में निरीक्षण करें।
>>>

SUMMARY G-W04-4:
<<<
लिबर ऑफिस इम्प्रेस में custom animation सीखने का ट्यूटोरियल है। पहले एक उदाहरण प्रस्तुति खोलें। फिर बाईं ओर के टेक्स्ट बॉक्स को चुनें और इन्सर्ट टास्क पैन में custom animation चुनें। इन्टरन्स टैब में डायगोनल चुनें और गति लॉव ले लें। फिर ऑक पर क्लिक करें। फिर एनीमेशन डायलॉग बॉक्स में बासिक टैब पर जाकर डायगोनल चुनें और गति मध्य ले लें। फिर ऑक पर क्लिक करें। दूसरे टेक्स्ट बॉक्स को चुनें और इन्सर्ट टास्क पैन में जोड़ें। फिर इन्टरन्स टैब में डायंड्राम चुनें और गति लॉव ले लें। फिर ऑक पर क्लिक करें। तीसरे टेक्स्ट बॉक्स को चुनें और इन्सर्ट टास्क पैन में जोड़ें। फिर इन्टरन्स टैब में डायगोनल चुनें और गति लॉव ले लें। फिर ऑक पर क्लिक करें। फिर एनीमेशन की क्रमबद्धता बदलने के लिए बेटवर बटन चुनें। फिर दिए गए विकल्पों में दिए गए विकल्पों को देखें। फिर दूसरे एनीमेशन पर डबल क्लिक करें और इफेक्ट ऑप्शंस डायलॉग बॉक्स देखें। फिर टाइमिंग टैब पर क्लिक करें और डेलेज फील्ड में दिलाई गई देरी को बढ़ाएं। फिर ऑक पर क्लिक करें। फिर पहले एनीमेशन पर फिर से डबल क्लिक करें और फिर इफेक्ट ऑप्शंस डायलॉग बॉक्स देखें।
>>>

Reply with 4 lines, each with exactly 10 digits.
```

## Window W05 (10 facts, 4 summaries)

```
FACTS:
1. Mozilla Thunderbird is a cross-platform email client capable of functioning across different operating systems.
2. Thunderbird allows users to download email messages from external accounts onto their local computer.
3. Using POP3 allows users to consolidate accounts into a single inbox inside Thunderbird.
4. Messages in Thunderbird can be grouped by attributes such as date, sender priority, or custom labels.
5. Mozilla Thunderbird can be installed on Ubuntu Linux using the Ubuntu Software Center.
6. In Ubuntu, Thunderbird is opened by typing thunderbird into Dash Home and clicking on the application icon.
7. Shortcut icons for Get Mail, Write, and Address Book are located beneath the main menu bar in Thunderbird.
8. The Thunderbird interface contains two panels, with the left panel showing account folders.
9. In Gmail, POP configuration settings are accessed under the Forwarding and POP/IMAP tab.
10. Enabling POP in Gmail involves selecting the enable POP option under POP download and saving the changes.

SUMMARY G-W05-1:
<<<
आपको मुजला थंडरबर्ड के बारे में सीखने का स्वागत है। यह एक सरल email client है और विभिन्न operating system पर कार्य कर सकता है। आप इसे उबंटू सॉफ्टवेयर सेंटर या मोजला वेबसाइट से डाउनलोड कर सकते हैं। आपको दो वैध email accounts होने चाहिए। थंडरबर्ड लॉन्च करने के लिए डेश घोंसला क्लिक करें और तारीख बांटने वाला बटन पर क्लिक करें। तब मेल अकाउंट सेटअप डायलॉग बॉक्स खुलेगा। इसमें आप अपने email accounts का निर्माण कर सकते हैं। उदाहरण के लिए, आप गूगल और यूहॉर्स एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट्रा एक्सट
>>>

SUMMARY G-W05-2:
<<<
इस टिटूरल में हम मुजला तन्डबाद के बारे में सीखते हैं। तन्डबाद डूँड संसता पिक करने और लांज कैसे करने की जानकारी मिलती है। यह एमेल अकाूँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँँ�
>>>

SUMMARY G-W05-3:
<<<
This tutorial introduces Mozilla Thunderbird, a simple email client available on various platforms. It covers downloading and launching Thunderbird, configuring new email accounts, reading and writing emails, and sending messages. Thunderbird supports multiple email accounts and categorizes messages by date, sender, priority, or custom labels. The tutorial demonstrates setting up Thunderbird on Ubuntu Linux 12.04. To install Thunderbird, users can use the Ubuntu Software Center or download it from the Mozilla website for Windows versions as well. For Thunderbird to work, users need at least two valid email addresses with POP3 enabled. Thunderbird launches via the Home button on the desktop, and its interface includes a main menu with options like Get Mail, Write, and Address Book. Thunderbird is divided into two panels; the left panel shows folders from configured accounts, while the right panel offers advanced features and options. The tutorial sets up two email accounts, stuserone@gmail.com and stusertwo@yahoo.com, both with POP3 enabled, to demonstrate the process.
>>>

SUMMARY G-W05-4:
<<<
Mozilla Thunderbird का परिचय और इसका डाउनलोड और संस्थापन शुरू करना सीखेंगे। Thunderbird एक सरल ईमेल क्लाईंट है जो विभिन्न ऑपरेटिंग सिस्टम पर काम करता है। इसे उबंटू सॉफ्टवेयर सेंटर या Mozilla वेबसाइट से डाउनलोड कर सकते हैं। इसके लिए आपको दो वैध ईमेल अकाउंट्स और इंटरनेट के जोड़ने की आवश्यकता होती है। Thunderbird लॉन्च करने के लिए डेस्कटॉप के बाएँ कोने के गोल बटन पर क्लिक करें। फिर मेल अकाउंट कॉन्फ़िगर करने के लिए डायलॉग बॉक्स खोलें। जीमेल या यूडोरा जैसे अन्य ईमेल अकाउंट्स से मेल डाउनलोड करने के लिए पॉप3 विकल्प को सक्षम करें। जीमेल अकाउंट में लॉगिन करें, फिर एड्रेस बार में www.gmail.com टाइप करें और जीमेल विंडो में settings आइकन पर क्लिक करें। फिर forwarding और pop imap टैब पर क्लिक करें और pop डाउनलोड में सभी मेल्स के लिए enable pop चुनें। सेटिंग्स विंडो में save changes पर क्लिक करें।
>>>

Reply with 4 lines, each with exactly 10 digits.
```

## Window W06 (10 facts, 4 summaries)

```
FACTS:
1. The stdio.h header file defines core input and output functions.
2. argc shows the total number of command line arguments provided to the program.
3. argc includes the actual name of the program in its count.
4. argv stores the actual arguments beginning from index 0.
5. Index 0 of argv contains the name of the program.
6. Index 1 of argv contains the first argument passed to the program.
7. The terminal is opened by pressing the Ctrl + Alt + T keys together.
8. The compilation command entered in the terminal is gcc main-with-args.c -o args.
9. Executing the program without arguments gives a total count of 1 because the zeroth argument is the executable filename itself.
10. Passing sunday, monday, and tuesday as arguments produces a total argument count of 4.

SUMMARY G-W06-1:
<<<
Namaskar, command line arguments ke baare mein aapke liye spoken tutorial mein swagat hai. Yahan hum ek example se start karenge, jisme main function ke saath arguments ka use karne mein jaanege. Main use kar rahe hoon Ubuntu OS version 11.10 aur GCC compiler version 4.6.1. Agar aap C programming se nahi parichay rakhte ho, to related tutorials ko aap website pe dekh sakte ho.

Main function mein, stdio.h aur stdlib.h header files se input-output functions aur library functions define hoti hain. Main function mein, argc program ke command line arguments ki sankhya dikhata hai, aur argv program ke actual name aur passed arguments ko store karta hai. Index 0 mein program ka name, index 1 se peeche passed arguments hoti hain. While loop arguments ki sankhya ko zindagi mein badhaata hai aur arguments ko print karta hai. Return 0 statement program ko exit karne mein madad karta hai.

Terminal mein Ctrl+Alt+T press karke open karein. GCC main-hyphen-args.c ke source file ko compile karne ke liye gcc main-hyphen-args.c -o args enter karein. Dot-slash args enter karein. Agar arguments nahi pass kiye hain to output mein arguments ki sankhya 1 hoti hai, zeroth argument program ka name hota hai, aur args hota hai.

Ab aap ek hi program mein do arguments pass karein, jaise: Sunday Monday Tuesday. Output mein arguments ki sankhya 4 hoti hai, zeroth argument program ka name, index 1 mein Sunday, index 2 mein Monday, aur index 3 mein Tuesday hoti hai.

Is tutorial se aap command line arguments ke use, argc, argv aur main function ke concept jaanege. Video ko dekho ya download karo, spoken tutorial project ke saarthakta hai.
>>>

SUMMARY G-W06-2:
<<<
नमस्कार! यह टॉटर्यल में हम एक सी प्रोग्राम सीखेंगे जो अर्गुमेंट्स को प्रिंट करता है। पहले हम अप्रेटिंग सिस्टम वर्ष्यन 11.10 और ग्ग्स कंपाइलर वर्शन 4.6.1 का इस्तेमाल करते हैं। हमारा पहला फायल `args.h` है, जो इनपुट और आउटपुट फंक्शन्स को परिबासित करता है। दूसरा फायल `stdlib.h` नंबरिक कन्वर्शन फंक्शन्स, सुडो रन्दम नंबर्स जैनरेशन फंक्शन्स, और अलोकेशन प्रोसेस कंट्रोल फंक्शन्स परिबासित करता है।

हमारा प्रोग्राम दो अर्गुमेंट्स लेता है: `argc` और `argv`. `argc` प्रोग्राम के अर्गुमेंट्स की संख्या देता है, जबकि `argv` अर्गुमेंट्स का एक चेन्जल लिस्ट देता है। प्रोग्राम नाम और पहला अर्गुमेंट को दिखाता है, फिर अर्गुमेंट्स की संख्या और उनकी सूची भी दिखाता है। अंत में, प्रोग्राम जीरो रिटन करता है।

अपने कंप्यूटर पर यह प्रोग्राम लिखकर और निष्पादित करके आप देख सकते हैं कि अर्गुमेंट्स कैसे प्रिंट होते हैं। यह टॉटर्यल आपको अर्गुमेंट्स का इस्तेमाल करने की तकनीक सीखने में मदद करता है।
>>>

SUMMARY G-W06-3:
<<<
Namaskar! Aapko command line arguments ke baare mein spoken tutorial mein swagat hai. Yahan hum ek example se start karte hain, jisme main function ke saath arguments ka use karenge. Main use kar rahe hoon Ubuntu operating system version 11.10 aur GCC compiler version 4.6.1. Agar aap C tutorials se nahi parichay rakhte hain, to related tutorials ko visit karein.

Main program mein ek code file open karte hain - main-hyphen-args.c. Yeh header files include karte hain - stdio.h (input-output functions), stdlib.h (numeric conversion, random number generation, memory allocation, etc.). Main function mein do arguments pass kiye gaye hain - int argc, char* argv[]. 

argc program mein command line arguments ki total number deta hai. argv[0] program ka naam hai, aur index 1 se argument start hota hai. Jaise, agar hum command line se arguments pass karte hain, toh argc uske count aur argv[1] se argument print hota hai.

Terminal mein GCC compiler use karte hain - gcc space main-hyphen-args.c space a-r-k-s space a-r-c-t-e-r-n-enter. Ab hum terminal mein output dekh sakte hain. Agar arguments nahi pass kiye hain, toh argc 1 aur argv[0] program ka naam deta hai.

Ab ek example dekhte hain - gcc main-hyphen-args.c space a-r-k-s space s-u-n-d-a-y space m-a-n-d-a-y space t-u-z-a-d-a-y enter. Ab output dekh sakte hain - total number of arguments are four, first argument is Sunday, arguments are Sunday Monday Tuesday.

Is tutorial se aap command line arguments ke use karna samajhenge, jo program ke naye naye possibilities provide karte hain. Video ko dekhen, project ko download karein.
>>>

SUMMARY G-W06-4:
<<<
This tutorial introduces command-line arguments in C programming using Ubuntu 11.10 and GCC compiler version 4.6.1. It explains how to pass arguments to the `main` function and process them within the program. The `argc` variable holds the number of command-line arguments, while `argv` is an array of strings containing the actual arguments. The first argument (`argv[0]`) is the program name, and subsequent arguments are the command-line inputs. The tutorial demonstrates this by compiling and running a sample program that prints all passed arguments. Initially, without any arguments, only the program name is displayed. After passing multiple arguments like "sunday", "monday", and "tuesday", the program correctly identifies and prints each argument, including the program name as the first argument. The key takeaway is understanding how to use `argc` and `argv` to handle different numbers of command-line arguments in C programs.
>>>

Reply with 4 lines, each with exactly 10 digits.
```

## Window W07 (10 facts, 4 summaries)

```
FACTS:
1. To activate change tracking, go to Edit, select Changes, and choose the Record option.
2. The Show option under Changes must be enabled to visibly record upcoming edits.
3. Newly inserted text appears in a different color.
4. Hovering the mouse over inserted text displays the editor's name, insertion date, and time.
5. The reviewer name attached to edits is determined by the username entered during LibreOffice installation.
6. Deleting text does not erase it immediately, but flags the line as marked for deletion.
7. Moving the cursor over deleted text displays the deletion message with reviewer name, date, and time.
8. LibreOffice Writer displays edits from different reviewers in distinct colors to distinguish their work.
9. Hovering over edited content in the document confirms whether additions and deletions were made by a specific peer.
10. A point concerning government institutions developing and promoting FOSS is added at the end of the document.

SUMMARY G-W07-1:
<<<
This tutorial explains how to perform peer review using LibreOffice Writer's document peer review feature. It starts by opening an existing document and enabling the "Record Changes" option for tracking edits. When changes are made, they are highlighted in a different color, showing who made them and when. Users can insert comments, delete text, or modify content, which appears clearly in the document. The reviewer can accept or reject these changes, and approved edits are included in the final document upon saving. The tutorial demonstrates this process using documents like "sevenreasonstoadoptfoss.odt" and "governmentsupportforfossinindia.odt". It shows how multiple reviewers can edit the same document, with each change highlighted differently. The tutorial also highlights how the system identifies the reviewer based on their username set during LibreOffice installation.
>>>

SUMMARY G-W07-2:
<<<
नमस्कार दोस्तों, लिबर ऑफिस राइटर में डॉक्यूमेंट का peer review कैसे करें यह टीटोरियल में समझाया गया है। आप एक मौजूद document को खोलकर देखेंगे। रिकॉर्ड चेंज्स विशेषता का उपयोग करके डॉक्यूमेंट का संपादन करेंगे। यह आपको समीक्षक द्वारा जोड़ी गई टिप्पणियों और बदलावों को देखने और स्वीकार करने में मदद देता है। यह लेखक द्वारा देखने और स्वीकार करने में भी मदद करता है। जब फाइल सेव हो जाती है, तो सभी संपादन और टिप्पणियां संहित हो जाती हैं। यहां हम लिनक्स ऑपरेटिंग सिस्टम और लिबर ऑफिस राइटर का उपयोग कर रहे हैं। डॉक्यूमेंट खोलकर रिकॉर्ड चेंज्स विशेषता को सेट करेंगे। बिंदु पर जाकर टिप्पणी करेंगे और टिप्पणी करने के लिए रिकॉर्ड विशेषता का उपयोग करेंगे। यह टिप्पणी करने और बदलाव करने में मदद करता है। एक से अधिक व्यक्ति एक समान document को संपादित कर सकते हैं। समीक्षक का नाम और रंग संपादन करने के लिए दिखाई देता है।
>>>

SUMMARY G-W07-3:
<<<
नमस्कार दोस्तों, लिबरऑफिस राइटर में डॉक्युमेंट का पीयर रिव्यू कैसे करें यह ट्यूटोरियल में समझाया गया है। आप एक मौजूद डॉक्युमेंट को खोलकर रिकार्ड चेंज्स ऑप्शन को सेट कर सकते हैं। इससे आगामी संपादन रिकार्ड होते हैं। आप नए टेक्स्ट जोड़ सकते हैं, टिप्पणी कर सकते हैं या बदलाव कर सकते हैं। समीक्षक नाम और टाइमस्टैम्प द्वारा डॉक्युमेंट में टिप्पणी किया गया व्यक्ति की पहचान दिखाई देती है। आप विलोपन या संपादन कर सकते हैं। एक से अधिक व्यक्ति एक समान डॉक्युमेंट को संपादित कर सकते हैं। लिबरऑफिस राइटर प्रत्येक संपादन को भिन्न रंग में दर्शाता है। आप टेक्स्ट पर माउस धुमा सकते हैं और समीक्षक का नाम देख सकते हैं। यह ट्यूटोरियल द्वारा समीक्षक द्वारा किए गए संपादनों को देखने का एक उदाहरण दिया गया है।
>>>

SUMMARY G-W07-4:
<<<
In this tutorial, you learn how to edit documents using LibreOffice Writer. You can add text, comment, delete, or modify text within the document. These changes become visible in the document and the author can easily see these edits. You use LibreOffice version 3.3.4 for this tutorial. To open a document, go to "File" > "Open" and select the file. For editing, insert a date and time stamp using the "Insert" menu. You can also change the name of the document based on its creation date. To delete text, highlight it and press the delete key. For example, you can type "Linux is a virus" repeatedly and then delete it to show the deletion timestamp. The document shows different colors for each editor's edits, with the reviewer's name highlighted when they edit. You can save the document and see that many edits and deletions have been made. This tutorial helps you understand how to effectively edit and manage documents in LibreOffice Writer.
>>>

Reply with 4 lines, each with exactly 10 digits.
```

## Window W08 (11 facts, 4 summaries)

```
FACTS:
1. Print Layout and Web Layout are the two primary view options in LibreOffice Writer.
2. The Web Layout option displays how the document will appear in a web browser.
3. Full screen mode is useful for editing documents and displaying them on a projector.
4. Pressing the Escape key exits Full Screen mode.
5. A new page break is inserted by choosing Insert, Manual Break, selecting Page Break, and clicking OK.
6. The Zoom and View Layout dialog box contains the headings Zoom Factor and View Layout.
7. The 'Fit width and height' option fits the document across the full length and width of the page.
8. The 100% view displays the page in its actual size.
9. A custom zoom factor can be entered in the Variable field.
10. Selecting the Automatic view layout option displays pages side by side.
11. The controls on the Writer status bar also permit changing the document's view layout and zoom.

SUMMARY G-W08-1:
<<<
लिबर ऑफिस वर्टर में डॉक्युमेन्ट्स को देखने और प्रिंट करने के लिए विभिन्न व्यापक विशेषताएँ सीखेंगे। दो मुख्य दृश्य विवरण हैं: प्रिंट लैयात और वेब लैयात। प्रिंट लैयात में डॉक्युमेन्ट प्रिंट होने पर कैसे दिखेगा दिखाता है, जबकि वेब लैयात में डॉक्युमेन्ट वेब ब्राउजर में कैसे दिखेगा दिखाता है। फुल स्क्रीन मोड के लिए विशेषता वाले विश्लेषण भी दिखाता है। डॉक्युमेन्ट में पेज जोड़ने के लिए मेन्यूबार में इंसर में मैनुअल ब्रेक चुनें और पेज ब्रेक चुनें। ज़ॉम विशेषता भी दिखाता है, जहाँ डॉक्युमेन्ट को देखने के लिए ज़ॉम फैक्टर बदला जा सकता है। विश्लेषण भी डॉक्युमेन्ट को पेज की लंबाई और चौड़ाई में फिट करने के लिए और विभिन्न पेजों को देखने के लिए उपयोगी है। वर्टर स्टेटस बार पर भी डॉक्युमेन्ट के दृश्य लेआउट और ज़ॉम को बदलने की अनुमति देता है।
>>>

SUMMARY G-W08-2:
<<<
This tutorial covers various view options in LibreOffice Writer for document viewing and editing. It explains how to switch between Print Layout and Web Layout views using the menu bar. For Print Layout, users click on View > Print Layout, and for Web Layout, they click on View > Web Layout. Full-screen mode can be accessed via View > Full Screen. To add a new page, users insert a manual page break. Zoom options allow adjusting the display size of the document, with features like Fit Width and Height, Fit to Width, and customizable zoom factors. The View Layout option lets users see different parts of the document on one or multiple pages. The status bar provides controls to change the view layout and zoom level, including icons for Single Column Mode and Book Mode.
>>>

SUMMARY G-W08-3:
<<<
लिबर ऑफिस राइटर में डॉक्यूमेंट्स को देखने और प्रिंट करने के लिए इस टूटोरियल में आपका स्वागत है। हम दो प्रकार के व्यू ऑप्शन सीखेंगे: प्रिंट लेयट और वेब लेयट। प्रिंट लेयट में डॉक्यूमेंट प्रिंट होने पर कैसे दिखेगा दिखाता है, जबकि वेब लेयट में डॉक्यूमेंट वेब ब्राउजर में कैसे दिखेगा दिखाता है। फुल स्क्रीन मोड डॉक्यूमेंट को बड़ा दिखाता है जब आप इसे संपादित करना चाहते हैं। डॉक्यूमेंट में पेज जोड़ने के लिए मैनु बार में इंसर में मैनुअल ब्रेक चुनें। ज़ॉम ऑप्शन में डॉक्यूमेंट को बड़ा या छोटा दिखाता है। व्यू लेयट ऑप्शन में डॉक्यूमेंट के विभिन्न पेजों को देखने और संपादित करने में मदद करता है। स्टेटस बार पर तीन कंट्रोल्स डॉक्यूमेंट के व्यू लेयट और ज़ॉम को बदलने में मदद करते हैं।
>>>

SUMMARY G-W08-4:
<<<
लिबर अप्विस राइटर में दोकिमेंच को प्रिंट करने और देखने के लिए यहां कुछ महत्वपूर्ण चीजें सीखेंगे। आपको अप्रेटिं सिस्टम का उपयोग करना है जो जेन्यु लिनाग स्वाद है। लिबर अपिस राइटर में पेविड व्यु अप्षन के बारे में सीखेंगे। जब आप एज्टीमर डोक्मेंट बनाने चाहते हैं, तो दोकिमेंच को अटिट करने के लिए फोई श्कीन मोड का उपयोग करें। दोकिमेंच को देखने के लिए पिंटल्याउड अप्षन बर ख्लिक करें। वेब लियाउड अप्षन के लिए मैनूबार में वियो अप्षन पर ख्लिक करें। दोकिमेंच को फुल श्कीन मोड में देखने के लिए फोई श्कीन मोड बर ख्लिक करें। जूम अप्षन दोकिमेंच को बड़ा या छोटा देखने के लिए उपयोगी है। पेज ब्रेक अप्षन दोकिमेंच में नए पेज जोड़ने के लिए उपयोगी है। जुम फैक्टर दोकिमेंच को फिट करने के लिए उपयोगी है। पेज विट या पेज हाइट अप्षन दोकिमेंच को विशिष्ट चवड़ाई या ऊँचाई में देखने के लिए उपयोगी हैं।
>>>

Reply with 4 lines, each with exactly 11 digits.
```

## Window W09 (11 facts, 4 summaries)

```
FACTS:
1. The Impress workspace has five tabs known as view buttons.
2. Notes view enables users to attach notes to each slide that do not show up during the presentation.
3. Handout view provides the capability to print slides as handouts and select how many slides appear per page.
4. The Slides pane on the left of the screen shows thumbnails of the presentation slides.
5. A new blank slide can be added after a selected slide by choosing Insert and then Slide.
6. A duplicate slide can be created by clicking Insert and then Duplicate Slide.
7. In Slide Sorter view, a slide can be copied and pasted after the final slide by selecting the After option.
8. Font family and font size can be adjusted using the text format toolbar.
9. A dialog box to customize font style and size can be opened by selecting Character under the Format menu.
10. Font color can be altered by clicking the down arrow situated next to the font color icon.
11. Text formatting options such as bold, italics, and underline can be applied using toolbar icons.

SUMMARY G-W09-1:
<<<
लिबर अफिस इंप्रस में प्रस्तुती बनाने के लिए आप जेन्यू लिनक्स और लिबर अपिस वर्जन 3.3.4 का उपयोग कर सकते हैं। आप नोर्मल टैब के द्वारा शुरू कर सकते हैं और फिर स्लाइट इंसर्ट कर सकते हैं। हाइलाइट नेल पर जाकर आप एक नया स्लाइट जोड़ सकते हैं। शीर्षक लिखने के लिए टेक्स्ट बार में खोलें और टेक्स्ट बार में टाइटल पर क्लिक करें। फिर शोड ताइप लगाएं और बाहर क्लिक करें। आप दो तरीकों से टेक्स्ट बार में लाइन जोड़ सकते हैं। एक तरीके से आप नए स्लाइट की पतिलिपी बना सकते हैं और दूसरे तरीके से आप फाँट और कलर बदल सकते हैं। टेक्स्ट फार्मेट तूल बार में फार्न टाइप और साइस टाइप बड़ा सकते हैं। आप भी दालोग बोक्स में फाँट और साईस सेट कर सकते हैं। फाँट को बदलने के लिए आप देवलप्मेंट स्लाइट को चुनकर बोरी टेक्स्ट बोक्स पर क्लिक करें और फाँट को बदल सकते हैं। आप भी टेक्स्ट को बोल्ड, इतालिक या अंडलान बना सकते हैं।
>>>

SUMMARY G-W09-2:
<<<
This tutorial covers how to create and format presentations using LibreOffice Impress on GNU/Linux with version 334. It explains the different views available in Impress, such as Normal, Outline, Notes, Handout, and Slide Sorter. Key features include inserting and duplicating slides, formatting fonts, and copying slides. To insert a new slide, select another slide, then click Insert > Slide. To duplicate a slide, click Insert > Duplicate Slide or right-click a slide, choose Copy, navigate to the desired location, and paste. For font formatting, double-click a slide, select the text box, and change the font style and size through the Text Formatting toolbar or the Format > Character dialog box. To change text color, select the text, click the Font Color icon, and choose a color from the dropdown menu. Bold, italic, and underline can also be applied using their respective icons.
>>>

SUMMARY G-W09-3:
<<<
लिबर ऑफिस इम्प्रेस में प्रस्तुति बनाने के लिए और बुनियादी फॉर्मेटिंग की तरह, इस ट्यूटोरियल में हम इम्प्रेस विंडो के भागों के बारे में सीखेंगे। इसमें विंडो के विभिन्न टेबल जैसे नोर्मल, ऑटलाइन, नोट्स, हान्डआउट और स्लाइड शॉर्ट व्यू बताएंगे। इसके अलावा, हम नए स्लाइड इंसर्ट करने, कॉपी करने और फॉन्ट फॉर्मेटिंग के तरीके सीखेंगे। फॉन्ट बदलने के लिए टेक्स्ट बॉक्स में चुनाव करें और फॉन्ट टाइप और साइज बदलें। फॉन्ट कलर बदलने के लिए फॉन्ट कलर आइकन का उपयोग करें। बोल्ड, इटालिक और अंडरलाइन भी फॉर्मेटिंग के लिए उपलब्ध हैं। स्लाइड को इंसर्ट करने के लिए दूसरे स्लाइड पर क्लिक करें और फिर इंसर्ट और ड्यूप्लिकेट स्लाइड चुनें। स्लाइड को कॉपी करने के लिए नोट्स व्यू में जाकर कॉपी और पेस्ट चुनें।
>>>

SUMMARY G-W09-4:
<<<
इस ट्यूटोरियल में हम लिबर ऑफिस impress में प्रस्तुति बनाने और बुनियादी formatting की शिक्षा सीखते हैं। हमने ग्नु लिनक्स और लिबर ऑफिस वर्जन 334 का उपयोग किया। प्रस्तुति में विभिन्न टैब जैसे नोट्स व्यू, नॉर्मल व्यू, ऑलटाइन व्यू, हान्डआउट व्यू और स्लाइड सोर्टर व्यू के बारे में सीखते हैं। स्लाइड इंसर्ट करने के लिए दूसरे स्लाइड पर क्लिक करें और फिर इंसर्ट और स्लाइड पर क्लिक करें। फॉन्ट और फॉन्ट को फॉर्मेट करने के लिए एक स्लाइड पर दबाएँ और फॉन्ट टूलबार में फॉन्ट टाइप और साइज़ बदलें। फॉन्ट को रंग बदलने के लिए भी उसी तरह कर सकते हैं। बॉल्ड, इटालिक और अंडरलाइन भी इसी तरह से लगा सकते हैं।
>>>

Reply with 4 lines, each with exactly 11 digits.
```

## Window W10 (11 facts, 4 summaries)

```
FACTS:
1. LibreOffice Impress is equivalent to Microsoft Office PowerPoint.
2. LibreOffice Impress is free, open-source software available at no cost for use and distribution.
3. GNU/Linux can be used as the operating system for LibreOffice Impress.
4. Users should choose the complete option when installing Impress.
5. The Impress window contains title bars, menu bars, standard bars, formatting bars, and status bars.
6. A presentation can be initiated from a template by choosing Recommendation of a Strategy.
7. Slide designs can be selected by choosing Presentation Backgrounds and then Blue Border.
8. Original can be chosen in the output medium field during presentation setup.
9. The presenter's name or organization name can be entered in the designated name field.
10. Impress presentations are saved with the Open Document Format odp extension.
11. A presentation can be closed by clicking File and then Close.

SUMMARY G-W10-1:
<<<
लिबर ऑफिस इम्प्रेस का परिचय और इसकी विशेषताओं के बारे में यह tutorial दिखाता है। इसमें लिबर ऑफिस इम्प्रेस का परिचय, विभिन्न टूलबार्स, नई प्रस्तुति कैसे तैयार करें, MS पावरपॉइंट के रूप में इसे सेव कैसे करें, और PDF डाक्यूमेंट कैसे ऑप्ट जाता है। इसका उपयोग स्वतंत्र और निशुल्क है। इंस्टैलेशन के लिए आप ग्नू लिनक्स या माइक्रोसॉफ्ट विंडोज का उपयोग कर सकते हैं। इम्प्रेस खोलने के लिए एप्लिकेशन्स, ऑफिस और इम्प्रेस पर क्लिक करें। नई प्रस्तुति तैयार करने के लिए फाइल, टेम्पलेट, रिकॉम्यूनेशन ऑफ एक स्ट्रेटेजी, प्रस्तुति बैकग्राउंड और डिजाइन चुनें। प्रस्तुति को सेवन करने के लिए फाइल और सेव पर क्लिक करें, और फिर इम्प्रेस ऑप्ट फाइल फॉर्मेट ऑडप के साथ सेव करें। MS पावरपॉइंट के रूप में इसे सेवन करने के लिए फाइल और ऑपन पर क्लिक करें और सैम्पल इम्प्रेस चुनें।
>>>

SUMMARY G-W10-2:
<<<
लिबर अफिस इंप्रस का परईचाय तूटूरिल में आपका स्वागत है। यह तूटूरिल में हम निम्न चीजें सीखेंगे:

1. लिबर अफिस इंप्रस का परईचाय इंप्रस में विविद तूलबार्स नहीं प्रस्तूती को तयार कैसे करें।
2. MS पार्पोंट में प्रस्थूटी करुब में सेव कैसे करें।
3. लिबर अफिस इंप्रस फ्री अपन्सोच्ट्विर है और उप्यो और वित्रन के लिए निशुल्क उप्लब्द है।
4. लिबर अफिस इंप्रस के साथ शुरुआत करने के लिए आप या तो मैकरुस्ट विन्डोस 2000 या अपने अपने वर्जन्स या लिबर अफिस वर्ज़न 3 3 4 का उप्योग कर सकते हैं।
5. लिबर अफिस इंप्रस को संस्तापित करने के लिए सनेप्टिक पैकेट मेनेजर का उप्योग करें।
6. नए प्रस्टिकी बनाने के लिए फायल बन कर अप्रिकेशन्स पर जाएं और फिर फायल बन कर लिबर अफिस इंप्रस पर क्लिक करें।
7. प्रस्टिकी को सेव करने के लिए फायल और सेव पर क्लिक करें।

इस तूटूरिल में आप लिबर अफिस इंप्रस का परईचाय और प्रस्टिकी को सेव करने की विविध ट्रिक्स सीखेंगे।
>>>

SUMMARY G-W10-3:
<<<
लिबर ऑफिस इम्प्रेस एक मुफ्त ओपन सोर्स सॉफ्टवेयर है जो माइक्रोसॉफ्ट पावरपॉइंट की तुलना में उपयोगी है। इसका संस्थापन लेबर ऑफिस सूट के लिए उपलब्ध है और इसे विंडोज या गनु लिनुक्स पर भी इस्तेमाल किया जा सकता है। इम्प्रेस में विभिन्न टूलबार्स हैं जैसे टाइल बार, मेन्यू बार, स्टैंडर्ड बार, फॉर्मेटिंग बार और स्टेटस बार। नई प्रस्तुति तैयार करने के लिए टूलबार्स का इस्तेमाल करें, फिर फाइल सेवा करें और डाक्यूमेंट को पीडीएफ में एक्सपोर्ट करें। लेबर ऑफिस मैनेजर का उपयोग सशक्त प्रस्तुतियों को तैयार करने के लिए किया जाता है। इम्प्रेस में प्रस्तुति तैयार करने के लिए टूटोरियल अनुसार ट्रेडिशनल प्रस्तुति तैयार करें और फिर इसे माइक्रोसॉफ्ट पावरपॉइंट में ओपन करें।
>>>

SUMMARY G-W10-4:
<<<
This tutorial introduces LibreOffice Impress, a free and open-source presentation software. It covers how to install and launch Impress on GNU/Linux using the LibreOffice suite. Key features include various toolbars such as Title Bars, Menu Bars, Standard Bars, Formatting Bars, and Status Bars. The tutorial demonstrates creating a new presentation by selecting a template, customizing it with a name, subject, and design, and saving it in the Impress format (ODP). It also explains how to open and save presentations in Microsoft PowerPoint format for compatibility. Additionally, the tutorial shows how to export a document to PDF within Impress. Overall, it guides users through the basics of creating and managing presentations in LibreOffice Impress.
>>>

Reply with 4 lines, each with exactly 11 digits.
```

## Window W11 (11 facts, 4 summaries)

```
FACTS:
1. The terminal can be opened by pressing the Ctrl, Alt, and T keys together.
2. JChemPaint is launched from the desktop by running the Java jar command in the terminal.
3. The lower toolbar includes buttons to enter an element symbol via keyboard and select a new drawing symbol from the periodic table.
4. Clicking the periodic table button opens the Choose an element window containing a built-in periodic table.
5. Hovering the cursor over an element like oxygen displays its information inside the info box.
6. The enter element text box allows users to type an element's symbol directly.
7. The show implicit hydrogens check box should be deselected in the preferences window if it is checked.
8. Single bonds to fluorine are initiated by clicking the fluorine button and the single bond button.
9. A small blue circle appears when placing the cursor over the xenon atom.
10. Right-clicking on the xenon atom opens its atom popup menu.
11. Selecting calcium from the alkali earth metals list replaces the xenon atom with calcium.

SUMMARY G-W11-1:
<<<
Namaskar propajee ap je kompet par is tutorial mein aapka swagat hai. Is tutorial mein hum neem neem se learn rahe hain periodic table aur abikriya banana. Ab prakar, yeh tutorial ko repeat karne ke liye main replay kar rahi hoon. Aapko Linux operating system version 12.04 je kompent aur version 3.3.1210 javeen version 7 basha banyan sehi hain. Je kompent kompetal structure aditor ke saath parichit ho jao. Je kompent window open karo, dono tarike se dekho. Dono tarike se, desktop pe terminal open karo. Terminal mein "cd /home/je-kompent" aur "java" type karo aur enter press karo. Ab periodic table trans se shukarate hain. Toolbaar ke niche wale elements ka list dekh sakte hain. Toolbaar par dhaane tarike se periodic table elements window open hoti hai. Yaha hum periodic table element text ke sath ek box dekh sakte hain. Yeh jarayani box hai jo element ki details dekhne mein madad karta hai. Jaise, cursor oxygen pe rakhe hai toh uske baare mein information box dekh sakte hain. Element window close karo, inter element symbol vaa window par click karo. Inter element text box open hota hai. Yahan element symbol type karo, example mein "jaan" type karo. Toolbaar par click karo, jaan symbol pradarachit hota hai. Ab jeon di pluriid ekspree se bahar elements banayein. Menu par jaen, functions par click karo aur periodic table window open hoti hai. Agar ye chhaye the, periodic table window close karo, floren inter button par click karo, aur fer single button par click karo. Cursor jean pe le aaye, is par nile avrit dikta hai. Mouse baim button click karo aur fer click karo, fer jean pluriid bond banane ke liye click karo. Ab jean ka atom pr right click karo, jean ka patam pradarachit hota hai. Is par iso tofs change element aur propajeez options ke baare mein samjhaenge. Ab iso tofs par jaen, jean ka iso tofs list window open hota hai. Je par cursor change element tak le aaye, aur uske baare mein ek sab menu open hota hai. Je par many shreniyos neche jaen, alkali metals list window open hota hai. Alkali metals se chhun, kalshiya se chhun, uska periodic table dekh sakte hain.
>>>

SUMMARY G-W11-2:
<<<
नमस्कार! इस tutorial में हम निम्न कुछ सीखेंगे: परिमाणी तendencies, अभिक्रिया बनाना, और rgroup query सेट करना। हम ubuntu लिनक्स OS का उपयोग करके jchempaint 3.3.1210 को चालू करेंगे। जानकारी box देखने के लिए अतिरिक्त buttons का उपयोग करें। अभियान्तर अवस्था तय करने के लिए periodic table का उपयोग करें। उदाहरण के लिए, जानकारी box में ऑक्सीजन के बारे में जानकारी देखें। अब ज़ेनॉन डाईफ्लूराइड का structure बनाएं। preferences में implicit hydrogens दिखाएं और fluorine के बांड बनाएं। फिर xenon के atom popup menu से isotopes और अन्य गुण देखें। alkali earth metals में calcium को चुनें। तो इस तरह हम अभियान्तर अवस्था तय करते रहेंगे।
>>>

SUMMARY G-W11-3:
<<<
This tutorial covers how to use the JChemPaint software for creating chemical structures and understanding periodic table trends. It starts by opening the JChemPaint window on Ubuntu Linux OS version 12.04 with Java version 7. Key steps include:

1. Opening the periodic table trends view.
2. Using the toolbar to add elements or select new drawing symbols.
3. Clicking "Enter an element symbol via keyboard" and then selecting a new drawing symbol from the periodic table.
4. Typing an element symbol in the text box and clicking OK to place it on the canvas.
5. Creating xenon difluoride (XeF2) by editing the structure using the preferences menu to show implicit hydrogens.
6. Drawing bonds between xenon and fluorine atoms.
7. Accessing the atom popup menu for xenon to change its isotopes and properties, such as switching to alkali earth metals like calcium.

The tutorial emphasizes navigating the interface and customizing chemical structures within JChemPaint.
>>>

SUMMARY G-W11-4:
<<<
नमस्कार, जेकैम्प चैप्टन पर यह tutorial में हम निम्न चीजें सीखेंगे: परियोडिक टेबल ट्रेंड्स, अभिक्रिया बनाना, और r ग्रुप क्वेरी सेट करना। हम ubuntu लिनक्स ऑपरेटिंग सिस्टम और जेकैम्प वर्सन तीन बिंदु तीन एस एक्स टू टू बिंदु एक्स टू एक्स टू एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स एक्स
>>>

Reply with 4 lines, each with exactly 11 digits.
```

## Window W12 (11 facts, 4 summaries)

```
FACTS:
1. The typedef keyword is used to provide symbolic names or aliases to existing or user-defined data types.
2. The syntax of typedef is typedef existing _ name alias _ name.
3. An example of typedef is typedef unsigned int uint;.
4. The palindrome program is compiled using the command gcc pallindrome.c -o pallindrome.
5. Executing the palindrome program with the input 121 yields the output that the given number is a palindrome number.
6. A union is a collection of different data types held together.
7. A union allocates a single, common storage space for all of its members.
8. Only one member of a union can be accessed at a time.
9. In union.c, a union named student is declared with the variables english, maths, and science.
10. A union variable named stud is declared inside the main function.
11. Running the compiled union program displays the output total is 228.

SUMMARY G-W12-1:
<<<
C में `typedef` और `union` के बारे में यहाँ कुछ महत्वपूर्ण बातें हैं। `typedef` कीवर्ड एक मौजूदा डेटा टाइप को एक उपनाम देने में मदद करता है। यह इसे लिखने और समझने में आसानी प्रदान करता है। उदाहरण के लिए, `typedef unsigned int uint;` द्वारा `unsigned int` को `uint` के रूप में उपयोग किया जा सकता है।

`union` एक डेटा टाइप है जो एक समान डेटा स्टोरेज स्पेस में अलग-अलग डेटा टाइपों को संग्रहित करता है। यह एक समान स्टोरेज स्पेस को सभी ऑर्डर्स में एक साथ निर्धारित करता है और एक समय में एक सिंगल ऑर्डर्स को अकेले एक्सेस किया जा सकता है। उदाहरण के लिए, `union stud { int english; int maths; int science; } stud;` द्वारा एक `union` बनाया जा सकता है।

`typedef` और `union` का उपयोग इसके लिए बहुत मददगार होता है कि कोड स्पष्ट और आसान रहे। यहाँ दिए गए उदाहरणों को देखकर आप इन बातों को बेहतर तरीके से समझ सकते हैं।
>>>

SUMMARY G-W12-2:
<<<
इस तोटर्यल में हम निम्न बारे में सीखते हैं: टाइप देफ की वर्ड और यून्यन टाइप। टाइप देफ की वर्ड एक उपनाम देती है जो एक वर्ड को अदद करती है और उसे आसान बनाती है। उदाहरण के लिए, हम एक नंबर को एक टाइप देफ की वर्ड के रूप में लिखते हैं। यून्यन टाइप भिन डेटा टाइप्स का कलेक्शन करता है और एक समान स्टोरेज स्पेस को निदारित करता है। हम एक यून्यन टाइप का उपयोग करके दो वेरिएबल्स को गोशित करते हैं। यहाँ एक उदाहरण है: हम एक फायल नाम उन्यन दोट्सी लिखते हैं और उन्यन टाइप को गोशित करते हैं। फिर हम एक फंक्षन लिखते हैं जो यून्यन टाइप का उपयोग करता है। यह टाइप देफ की वर्ड और यून्यन टाइप के बीच अंतर दिखाता है।
>>>

SUMMARY G-W12-3:
<<<
This tutorial covers `typedef` and `union` in C programming using Ubuntu 11.10 with GCC version 4.6.1. `typedef` allows users to assign a new name to an existing data type or user-defined type, making the code more readable and easier to modify. An example of `typedef` is `typedef unsigned int uint`. The tutorial demonstrates this by checking if a given number is a palindrome, where `uint` is used as an alias for `unsigned int`.

The tutorial then introduces `union`, which groups different data types into a single entity but allocates the same storage space for all its members. Only one member can be accessed at a time. An example shows calculating the total marks of a student using a `union` to store different subjects' marks. The program calculates the total marks as 228 when run.

The tutorial also highlights the difference between `union` and `structure`—unions allocate the same storage space for all their members, whereas structures allocate separate spaces for each member.
>>>

SUMMARY G-W12-4:
<<<
इस tutorial में हम टाइप डिफ़ (typedef) और यूनियन (union) के बारे में सीखते हैं। टाइप डिफ़ का उपयोग मौजूदा डेटा टाइपों को उपनाम देने में किया जाता है, जो कोड को स्पष्ट बनाता है। उदाहरण के लिए, `typedef unsigned int uint` लिखने की जगह `uint` लिखना आसान होता है। यूनियन दो या अधिक डेटा टाइपों को एक साथ स्टोर करता है, लेकिन एक समय में एक सिंलेक्स डेटा टाइप को अकेले उपयोग किया जा सकता है। उदाहरण के लिए, `union student { int english; int maths; int science; } stud;` यहाँ `stud` यूनियन वेरिएबल द्वारा एक साथ तीन डेटा टाइपों को स्टोर करता है। यूनियन और स्ट्रक्चर के बीच अंतर यह है कि स्ट्रक्चर अपने सभी डेटा टाइपों के लिए अलग-अलग स्टोरेज स्पेस निर्धारित करता है, जबकि यूनियन सभी डेटा टाइपों के लिए एक साथ स्टोरेज स्पेस निर्धारित करता है।
>>>

Reply with 4 lines, each with exactly 11 digits.
```

## Window W13 (11 facts, 4 summaries)

```
FACTS:
1. JChemPaint is a 2D chemical structure editor and viewer.
2. JChemPaint is a free and open-source cross-platform application developed in Java.
3. JChemPaint allows importing and exporting structure data in plaintext formats such as SMILES, Molfile, CML, and InChIKeys.
4. Java must be installed on the system to run JChemPaint.
5. Java can be installed on Ubuntu using the Synaptic Package Manager.
6. The downloaded JChemPaint file should be moved from the Downloads folder to the Desktop.
7. The terminal on Ubuntu can be opened by pressing Ctrl, Alt, and T together.
8. Typing 'cd desktop' and pressing Enter navigates to the Desktop directory in the terminal.
9. Running the Java jar command in the terminal launches the JChemPaint window.
10. JChemPaint can only be opened from the terminal.
11. On Windows, Java Runtime Environment 7 is installed by accepting the license agreement and choosing the executable installer link.

SUMMARY G-W13-1:
<<<
नमस्कार! इस tutorial में हम jchempaint के बारे में सीखेंगे। यह एक 2D चेमिकल स्ट्रैक्चर्स इडिटर और व्यूअर है, जो फ्री और ऑपन स्रोट एप्लिकेशन है। इसको उबन्टु OS 1204 और विंडोज में संस्थापित कर सकते हैं।

उबन्टु पर, हम फायरफॉक्स ब्राउजर खोलते हैं और जाँचते हैं कि jchempaint का डाउनलोड पेज पर जाएं। जरीर जानकारी के लिए, जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी जरी ज
>>>

SUMMARY G-W13-2:
<<<
नमस्कार! इस टूटर्यल में जे खेंपेंट को विंडूस अपरेटिंग सिस्टम पर स्थापित करने और इसका उपयोग करके स्तुक्छर्स बनाने की विधि सीखेंगे। आपके पास इंटनेड कनेक्शन, सनेप्टिक पैकेज मेनेजर, और तरमिनल की जरूरत होगी। जे खेंपेंट एक 2D केमिकल स्वक्षर अदिटर है जो जावा में लिखा गया है।

स्थापना के लिए, आप फायरफैक्स ब्राउजर खोलेंगे और जे खेंपेंट के डाउनलोड पेज जाएंगे। जे खेंपेंट जार फायल डाउनलोड करेंगे और इसे सेप फायल में खोलेंगे। तरमिनल में जावा में जे खेंपेंट को चार्टर करेंगे। फिर विन्टोस पर जावा संस्तापित करेंगे और जे खेंपेंट को विंडोस में संस्थापित करेंगे। यह तरीके से आप जे खेंपेंट का उपयोग करके स्तुक्छर्स बना सकते हैं।
>>>

SUMMARY G-W13-3:
<<<
This tutorial introduces JChemPaint, a free and open-source 2D chemical structures editor and viewer developed in Java. It covers installation on both Ubuntu OS 12.04 and Windows 7. Key steps include downloading the latest JChemPaint JAR file from GitHub and saving it to the desktop. On Ubuntu, users then open a terminal, navigate to the desktop directory, and run `java -jar jchempaint331210.jar` to launch JChemPaint. For Windows, users download the Java SE Runtime Environment 7, install it, and subsequently download and run JChemPaint. The tutorial also highlights the importance of having Java installed for JChemPaint to function properly. Additionally, it explains how to use JChemPaint's interface, including its menu bar, toolbars, panels, and preferences, to create and save molecular structures with .mol file extensions.
>>>

SUMMARY G-W13-4:
<<<
नमस्कार! इस tutorial में हम jcampaint के बारे में सीखेंगे। यह एक फ्री और ओपन सोर्स क्रॉस प्लेटफॉर्म एप्लीकेशन है जो जावा में विकसित है। यह चामकों और स्ट्रक्चर्स को संस्थापित करने और संस्थापित करने में मदद करता है।

ओबंटू ऑपरेटिंग सिस्टम पर jcampaint संस्थापित करने के लिए, आप फायरफॉक्स ब्राउजर खोलें और जेकैम्पेंट के डाउनलोड पेज पर जाएं। आप जेकैम्पेंट डाउनलोड कर सकते हैं। फिर आप डाउनलोड की हुई फाइल को डेस्कटॉप पर सेव कर सकते हैं। टर्मिनल में जे कैम्पेंट रन करने के लिए जावा जार फाइल को खोलें।

विंडोज पर jcampaint संस्थापित करने के लिए, आप फायरफॉक्स ब्राउजर खोलें और जे एसई रनटाइम एनवायरमेंट डाउनलोड करें। फिर आप जे कैम्पेंट जार फाइल को खोलें। यहाँ तक कि जे कैम्पेंट विंडो खुलने के लिए टर्मिनल में कुछ कमांड दर्ज करने की जरूरत होती है।
>>>

Reply with 4 lines, each with exactly 11 digits.
```

## Window W14 (11 facts, 4 summaries)

```
FACTS:
1. The demonstration uses Ubuntu 12.04 and Mozilla Thunderbird 13.01.
2. A new folder can be initiated by right-clicking an email account and choosing the new folder option.
3. Emails can be moved from the inbox to the important mails folder via drag and drop.
4. Clicking search messages under advanced features launches the message search interface.
5. Search criteria can be set to query messages matching a particular subject term such as ten interesting.
6. A filter is a rule applied to organise and sort messages within a mailbox.
7. Selecting manage message filters in advanced features displays the message filters dialog box.
8. A filter action can be configured to move matching messages to a selected folder.
9. Clicking run now applies the newly created filter immediately to the mailbox.
10. Thunderbird configures Gmail accounts automatically, but other email accounts must be configured manually.
11. POP functionality must be enabled inside the Yahoo account before configuring it in Thunderbird.

SUMMARY G-W14-1:
<<<
इस ट्यूटोरियल में आपको अधिक जानकारी दी गई है कि आवास्टित फिल्टर्स कैसे नियत करें और फिल्टर्स कैसे इस्तामिल करें। आप अपने इमेल अकाउंट की सेटिंग्स बड़ना और एक नया फिल्टर बनाना सीखेंगे। आप अपने इमेल अकाउंट से दूरी मेलों को इनबॉक्स या अप्डॉरी मेलों में फिल्टर कर सकते हैं। फिल्टर नाम और सब्जेक्ट चुनकर आप विशिष्ट मेलों को फिल्टर कर सकते हैं। फिल्टर नियम बनाने के लिए ब्रूश बॉक्स और फिल्टर रूल्स डालने के बाद आप फिल्टर नाम और सब्जेक्ट दर्ज कर सकते हैं। फिर फिल्टर बनाने के लिए बॉक्स चुनकर आप फिल्टर बनाने के लिए बॉक्स चुन सकते हैं। फिर फिल्टर बनाने के लिए बॉक्स चुनकर आप फिल्टर बनाने के लिए बॉक्स चुन सकते हैं। फिर फिल्टर बनाने के लिए बॉक्स चुनकर आप फिल्टर बनाने के लिए बॉक्स चुन सकते हैं। फिर फिल्टर बनाने के लिए बॉक्स चुनकर आप फिल्टर बनाने के लिए बॉक्स चुन सकते हैं। फिर फिल्टर बनाने के लिए बॉक्स चुनकर आप फिल्टर बनाने के लिए बॉक्स चुन सकते हैं। फिर फिल्टर बनाने के लिए बॉक्स चुनकर आप फिल्टर बनाने के लिए बॉक्स चुन सकते हैं। फिर फिल्टर बनाने के लिए बॉक्स चुनकर आप फिल्टर बनाने के लिए बॉक्स चुन सकते हैं। फिर फिल्टर बनाने के लिए बॉक्स चुनकर आप फिल्टर ब
>>>

SUMMARY G-W14-2:
<<<
This tutorial covers configuring account settings and email accounts using Thunderbird on Ubuntu 12.04. It explains how to add folders to an email account, such as creating a "Important Mails" folder by right-clicking on the Gmail account and selecting "New Folder." You can then drag and drop emails into this folder. Advanced filtering options allow you to search for specific messages based on criteria like subject or date. For example, you can create a filter to move all emails with "Thunderbird" in the subject to the "Important Mails" folder. Additionally, the tutorial demonstrates configuring Yahoo accounts manually since they don't configure automatically like Gmail. It guides users through logging into their Yahoo account, opening a new browser tab, and entering the Yahoo URL to set up the POP server.
>>>

SUMMARY G-W14-3:
<<<
इस ट्यूटोरियल में हम ईमेल अकाउंट का कन्फिगरेशन और फोल्डर्स का जोड़ना सीखते हैं। थंडरबर्ड विंडो खोलने के लिए लॉन्चर में थंडरबर्ड इक्न चाहिए। फोल्डर्स जोड़ने के लिए अकाउंट से चुनें, फिर दाएँ क्लिक करके नया फोल्डर चुनें। मैसेज खोजने के लिए एडवांस्ड फिल्टर्स चाहिए, जैसे विशिष्ट शब्द या तिथि के अनुसार। थंडरबर्ड से विभिन्न ईमेल अकाउंट्स का संचालन कर सकते हैं। याहू अकाउंट को कन्फिगर करने के लिए याहू वेबसाइट पर लॉगिन करना और फिर थंडरबर्ड में याहू अकाउंट जोड़ना चाहिए।
>>>

SUMMARY G-W14-4:
<<<
इस ट्यूटोरियल में हम सीखते हैं कि गूगल गैल्टी और याहू गैल्टी अकाउंट्स को थंडरबर्ड में कैंfigरेट कैसे करें। थंडरबर्ड विंडो खोलने के लिए थंडरबर्ड इक्यांस क्लिक करें। गैल्टी अकाउंट जोड़ने के लिए अकाउंट स्टेट्स चुनें और न्यू फोल्डर चुनें। फोल्डर डायलॉग बॉक्स में इम्पोर्टेंट मेल्स नाम दें और फोल्डर बनाएं। याहू अकाउंट को कैंfigरेट करने के लिए याहू इन्टरनेट ब्राउजर खोलें और याहू एड्रेस बार में याहू डॉट इन टाइप करें। थंडरबर्ड में एडवांस्ड फीचर्स चुनकर मेल फिल्टर्स निर्धारित करें। फिल्टर नाम में सब्जेक्ट थंडरबर्ड लिखें और फिल्टर रूल्स डायलॉग बॉक्स में फिल्टर निर्धारित करें। फिर फोल्डर इम्पोर्टेंट मेल्स चुनें और फिल्टर रन नाव पर क्लिक करें।
>>>

Reply with 4 lines, each with exactly 11 digits.
```

## Window W15 (10 facts, 4 summaries)

```
FACTS:
1. The demonstration is performed using the GNU/Linux operating system and LibreOffice suite version 3.3.4.
2. Aligning text to the left positions it along the left margin of the document page.
3. Justify alignment evenly spaces text between the left and right margins of the page.
4. Bullets and numbering can be accessed through the Format option on the menu bar.
5. Pressing the Enter key automatically inserts a new bullet point or incremental number.
6. The Tab and Shift keys are used to increase and decrease indentation levels for bullets.
7. Bullets and numbering can be disabled by selecting the Numbering Off option.
8. Text can be copied by selecting it, right-clicking, and clicking the copy option.
9. The keyboard shortcut to copy text is Ctrl + C.
10. The keyboard shortcut to paste text is Ctrl + V.

SUMMARY G-W15-1:
<<<
This tutorial covers basic text alignment and formatting in LibreOffice Writer. It starts by opening an existing document named "resume" and demonstrates how to align text to the left, right, or justify it using the alignment tools. The tutorial then explains how to add bullets and numbering to create a structured list of points, which can be customized through the bullets and numbering dialog box. It also shows how to indent text and toggle these features on and off. Additionally, the tutorial teaches how to copy and paste text within the document using both mouse commands and keyboard shortcuts (Ctrl+C for copy, Ctrl+V for paste). Overall, the session aims to make documents more visually appealing and easier to read by applying these formatting techniques.
>>>

SUMMARY G-W15-2:
<<<
इस ट्यूटोरियल में हम नियमित टेक्स्ट आरेख, बुलेट्स, क्रमांकन, और फाउंट फॉर्मेटिंग की तरह कई महत्वपूर्ण विषयों सीखते हैं। हम गनु लिनक्स ऑपरेटिंग सिस्टम और लिबर ऑफिस विंडोज वर्सन तीन बिंक चार में एक नया डॉक्यूमेंट खोलते हैं। टेक्स्ट आरेख के लिए लाइन लेवर चुनते हैं - लेवर लेवर, राइट लेवर और जस्टिफाइ। बुलेट्स और क्रमांकन भी इस तरह की टेक्स्ट के लिए उपयोगी होते हैं। हम टेक्स्ट को कॉपी करके पेस्ट कर सकते हैं और ट्रिक्स लाइन और इंडेंट टेक्स्ट को विस्तार या घटाने के लिए भी उपयोग कर सकते हैं। Ctrl C और Ctrl V श्रॉट क्युटर्स भी उपलब्ध हैं।
>>>

SUMMARY G-W15-3:
<<<
आप राइटर में एक नया डोक्यमेंट खोल सकते हैं। फिर आप शब्द चुनकर अलाईन लेफ्ट या रिज्यूम पर क्लिक कर सकते हैं। यह शब्द दाई या बाई अलाईन हो जाता है। आप बूलेट्स और नमबरिंग उप्योग कर सकते हैं जब आपके पास टेक्स्ट की लाईन या पाराग्राफ हो। आप नए बूलेट्स और नमबरिंग जोड़ सकते हैं और उन्हें बंद कर सकते हैं। आप नेम कोलन या शिप्ट उप्योग कर सकते हैं। आप डोक्यमेंट में नेम शब्द दोबा ताएप कर सकते हैं और फिर उसी टेक्स्ट को लिख सकते हैं। आप कोपी और पेस्ट अप्यों कर सकते हैं और नेम शब्द फिर से लिख सकते हैं। कोपी करने के लिए कंट्रोल सी और पेस्ट करने के लिए कंट्रोल वी शॉर्ट कट के रूप में उपलब्ध हैं।
>>>

SUMMARY G-W15-4:
<<<
लिबर ऑफिस लाइटर में टेक्स्ट अलाइनिंग, बुल्लेट्स और क्रमांकन जैसी बुनियादी विशेषताओं का उपयोग करें। पहले नए डॉक्यूमेंट खोलें और टेक्स्ट को अलाइनिंग करें। टेक्स्ट को लाइंग्वर, राइट या जस्टिफाइ कर सकते हैं। बुल्लेट्स और क्रमांकन जोड़ने के लिए फॉर्मेट मेन्यू में बुल्लेट्स और क्रमांकन चुनें। टैब और शिफ्ट टैब टैबिंग करने में मदद करते हैं। कोपी और पेस्ट जैसी विशेषताओं का उपयोग करने के लिए कोपी करने के लिए कंट्रील + सी और पेस्ट करने के लिए कंट्रील + वी ट्रिक्स शामिल हैं।
>>>

Reply with 4 lines, each with exactly 10 digits.
```

## Window W16 (12 facts, 4 summaries)

```
FACTS:
1. The demonstration uses Ubuntu Linux OS version 11.10 and GCC compiler version 4.6.1.
2. Storage class specifiers inform the compiler where to store a variable.
3. The syntax for storage class specifiers consists of the storage specifier, data type, and variable name.
4. The auto keyword declares an automatic variable that has local scope.
5. Automatic variables are not initialized automatically and must be initialized explicitly during declaration.
6. The storage space for auto variables is CPU memory.
7. Declaring an auto variable globally outside a function produces a file scope declaration error.
8. An auto variable cannot be initialized globally because it is local to a function.
9. Static variables are initialized to zero.
10. Static variables are not destroyed even after program control exits a block.
11. The value of a static variable is retained across different function calls.
12. The storage space for static variables is CPU memory.

SUMMARY G-W16-1:
<<<
इस टुटोरियल में हम स्टोरेज क्लास स्पेसिफायर्स के बारे में सीखते हैं। स्पेसिफायर्स निर्दिष्ट करते हैं कि वेरिबल कहाँ संचित होंगी, कैसे संचित होंगी और उनकी शुरुआती वैल्यू क्या होती है। इनमें auto, static, extern और register कीवर्ड शामिल हैं।

auto कीवर्ड लोकल स्कोप में वेरिबल घोषित करता है और इनिशियलाइज्ड नहीं होता है। एक उदाहरण में देखा गया कि auto वेरिबल i में इनिशियलाइज्ड नहीं होता और इसलिए एरर दिखाई देता है। static कीवर्ड वेरिबल को ग्लोबल स्कोप में रखता है और इनिशियलाइज्ड होता है। इसलिए, एक static वेरिबल i को जीरो से इनिशियलाइज्ड किया गया है और इसलिए इसका उत्पादन जीरो होता है।
>>>

SUMMARY G-W16-2:
<<<
This tutorial introduces storage class specifiers in C programming, explaining how they instruct the compiler on where to store variables, their initial values, and their lifetimes. The key specifiers discussed are `auto` and `static`.

`Auto` specifies that a variable is local to a function and must be initialized each time the function is called. An example demonstrates this by declaring an `auto` variable `i` within a function named `increment`. When compiled without initialization, it results in an error because `auto` variables are local and cannot be globally initialized. Initializing `i` to `0` before calling `increment` resolves this issue, as shown in the terminal output.

`Static` variables, also introduced briefly, are initialized to `0` and retain their value between function calls, occupying CPU memory. An example modifies the previous code file to demonstrate `static` initialization, ensuring the variable retains its value across multiple function calls, as verified by the terminal output showing consistent `0` values.
>>>

SUMMARY G-W16-3:
<<<
Storage class specifiers के बारे में इस tutorial में सीखेंगे। इन्हें compiler को बताते हैं कि वेरिएबल कहाँ संचित करना है, कैसे सेव करना है, और वेरिएबल की शुरुआती वैल्यू क्या होती है। इन्हें दो प्रकार के होते हैं: auto और static। Auto कीवर्ड लोकल स्कोप में वेरिएबल को घोषित करता है और इनिशियालाइज़ करना आवश्यक है। Static कीवर्ड भिन्न फंक्शन कल्स के बीच वेरिएबल की वैल्यू को रखता है। उदाहरण के लिए, auto वेरिएबल i को फंक्शन में घोषित किया गया था और इनिशियालाइज़ किया गया था। फिर static वेरिएबल को देखा गया था और इनिशियालाइज़ होता है जब प्रोग्राम को बंद किया जाता है। यह tutorial द्वारा दिए गए उदाहरणों से यह सीखा जा सकता है कि इन्हें कैसे इनिशियालाइज़ किया जाता है और कैसे फंक्शन में लोकल या प्रोग्राम के लिए ग्लोबल रखा जाता है।
>>>

SUMMARY G-W16-4:
<<<
स्तोरेज क्लास स्पैसीटार्स में वेरेबिल और स्टाटिक वरेबिल के बारे में बात की गई। वेरेबिल वर्ट लोकल स्कोप में होते हैं और इनिशिलाइज किए जाने पर अटोमेटिक रूप से शुरू होते हैं। उबन तो अप्रेटिंग सिस्टम पर उबन्तु और उबन तो अप्रेटिंग सिस्टम पर उबन्तुपर जीसीसी कंपालर पर इस टूर्याल के लिए इन्स्टॉल किया गया है। अटो वेरेबिल फुंक्शन में इनिशिलाइज किए जाने पर लोकल स्कोप में रहते हैं। अपने प्रोग्राम में अटो वेरेबिल फुंक्शन को गोशित करने के लिए निश्पादन करें। स्टाटिक वरेबिल फुंक्शन कोल्स के बीच रहते हैं और नश्ट नहीं होते हैं। इन्स्टॉल करने के बाद फुंक्शन को निश्पादित करने के लिए तामिनल पर निष्पादन करें। स्टाटिक वरेबिल को निश्पादित करने के लिए फिर से फुंक्शन को निष्पादित करें।
>>>

Reply with 4 lines, each with exactly 12 digits.
```

## Window W17 (10 facts, 4 summaries)

```
FACTS:
1. Notes in Impress serve as additional reference material for the audience or as cues to assist the presenter during a talk.
2. Clicking on the Notes tab displays a notes text box below the slide for typing notes.
3. Notes text can be formatted directly using the font type dropdown, font size dropdown, and bullet icon.
4. To create standard formatting for all notes, open the Notes Master by clicking View, then Master, and selecting Notes Master.
5. There is a notes master for each master slide utilized in the presentation.
6. Formatting preferences set on the notes master apply automatically to all notes throughout the presentation.
7. Text formatting in the notes master can be adjusted by choosing options such as font size 32 and red font color under Character dialog box.
8. Shapes such as an isosceles triangle can be added from Basic Shapes on the drawing toolbar to act as a logo.
9. A shape's fill color can be modified via Area in the context menu by selecting Color and choosing Blue 7.
10. Moving the slide placeholder towards the top of the screen creates more space to resize the notes placeholder.

SUMMARY G-W17-1:
<<<
लिबर ऑफिस इम्प्रेस में प्रे�zentेशन नोट्स के बारे में और उन्हें प्रिंट कैसे करना सीखेंगे। नोट्स दो उद्देश्यों के लिए होते हैं: दर्शकों के लिए और उद्घोषक को रिफरेंस देने के लिए। प्रस्तुति खोलें, शीर्षक स्लाइड चुनें और टेक्स्ट बदलें। नोट्स जोड़ने के लिए नोट्स टेबल चुनें, नोट्स बॉक्स में टाइप करें और "नोट्स जोड़ें" पर क्लिक करें। नोट्स में टेक्स्ट को फॉर्मेट करने के लिए फॉन्ट टाइप और आकार बदलें। नोट्स मास्टर बनाने के लिए मुख्य मेनू से व्यू पर क्लिक करें और फिर मास्टर पर क्लिक करें। नोट्स मास्टर बनाने के लिए नोट्स मास्टर पर क्लिक करें। नोट्स मास्टर व्यू में नोट्स के फॉर्मेट निर्धारित करें। नोट्स प्लेस होल्डर और स्लाइड प्लेस होल्डर का आकार बदलने के लिए नोट्स प्लेस होल्डर चुनें और इसे स्क्रीन के ऊपर ले जाएं।
>>>

SUMMARY G-W17-2:
<<<
This tutorial covers how to use presentation notes in Microsoft Impress, a free alternative to PowerPoint. Notes can serve two purposes: providing additional content or references for speakers on each slide, or offering notes for the audience. To add notes, select the "Notes" tab, click on the notes text box below the slide, and start typing. For formatting text, choose the desired font type and size from the Impress window's top-left corner. Bullet points can be added using the bullet icon. To create a notes master, go to the main menu, click on "View," then "Master," and finally "Notes Master." This sets a standard format for all notes in the presentation. Notes can be formatted individually or according to the master settings. Additionally, you can add logos and shapes to notes by selecting them from the drawing toolbar, customizing their appearance through the formatting options.
>>>

SUMMARY G-W17-3:
<<<
लिबर ऑफिस impress में presentation notes कैसे लिखें और प्रिंट करें याद करेंगे। नोट्स दो उद्देश्यों के लिए लगातार लिखे जाते हैं: दर्शकों के लिए प्रत्येक slide पर अतिरिक्त सामग्री या रेफ्रेन्सेस और उद्घोषक को reference notes के ज़रिये मदद करने के लिए। नोट्स जोड़ने के लिए नोट्स टैब पर क्लिक करें और नोट्स टेक्स्ट बॉक्स में टाइप करें। नोट्स में टेक्स्ट को फॉर्मेट करने के लिए फॉंट टाइप और फॉंट साइज बदलें। नोट्स में बुलेट पॉइंट जोड़ने के लिए बुलेट इक्सोन क्लिक करें। नोट्स में मास्टर बनाने के लिए मुख्य मेनू से व्यवस्था पर क्लिक करें और फिर मास्टर पर क्लिक करें। नोट्स में लॉगो जोड़ने के लिए ड्राइंग टूलबार से बेसिक शेप्स पर क्लिक करें और इसोसिलिस ट्रिकोन चुनें। नोट्स टेक्स्ट बॉक्स के ऊपरी बाएँ कोने पर ट्रिकोन प्रविष्ट करें और इसे अक्षर क्षेत्र में रंग और फॉर्मेटिंग करें।
>>>

SUMMARY G-W17-4:
<<<
लिबर अफिस इंप्रस में नोट्स प्रिंट करने और नोट्स बनाने की टीटूल दी गई। नोट्स दो उदेश्वागत दर्शकों के लिए होते हैं - एक्स्ट्रा सामग्री या रेफ्रन्स के लिए रेफ्रन्स नोट्स। नोट्स जोड़ने के लिए नोट्स टैप पर क्लिक करें। नोट्स बॉक्स में टाइप करें। नोट्स मास्टर बनाने के लिए मैनु में क्लिक करें। नोट्स मास्टर व्यू देखें। नोट्स मास्टर व्यू में नोट्स स्लाइड ताइप करें। नोट्स प्रिंट करने के लिए नोट्स पाटख के निचे क्लिक करें। नोट्स में फार्मेटिंग करने के लिए नोट्स मास्टर व्यू में चुनें। नोट्स प्रिंट करने के लिए नोट्स प्लेस हुल्टर चुनें। नोट्स प्लेस हुल्टर बड़ाने के लिए बाया माँस बतन दबाएं।
>>>

Reply with 4 lines, each with exactly 10 digits.
```

## Window W18 (11 facts, 4 summaries)

```
FACTS:
1. The demonstration runs on the GNU/Linux operating system using LibreOffice suite version 3.3.4.
2. The Find and Replace feature searches for text and can replace text throughout the document.
3. Find and Replace can be accessed by clicking the Edit option and then selecting Find and Replace.
4. Clicking Find All highlights every occurrence of the specified search text across the document.
5. Clicking Replace All substitutes every instance of the searched text with the replacement text.
6. The backwards option in Find and Replace searches through text from the bottom upward.
7. Spellcheck is used to detect spelling errors across the entire document or within a selected portion of text.
8. Spellcheck checks for spelling errors and provides the option to add an unrecognized word to the user dictionary.
9. Language configuration is accessed by clicking Tools on the menu bar and selecting Options.
10. Under the Default languages for documents settings, the Western language field is changed to English USA.
11. The AutoSpellcheck option must be enabled on the toolbar to utilize spelling and grammar checking.

SUMMARY G-W18-1:
<<<
लिबर अफिस राइटर में फाँई और इप्लेस विशेषताओं का इस्तेमाल सीखेंगे। फाँई टेक्स्ट को बड़ाता है या पूरे डोक्यमेंट में टेक्स्ट को बदलता है। इसके लिए रिज्यूम दोड फायल खोलें, फिर एडिट अप्शन पर क्लिक करें, फिर फाइट आन रीपलेस पर क्लिक करें। फिर स्टॉन्ट टूल बार में बटन पर क्लिक करें और जिस टेक्स्ट को बदलना चाहते हैं उसको सर्च फील में लिखें। उदाहरण के लिए, रामेश को रामेश को बदलना चाहते हैं। फिर रिपलेस विट टैब में मनीश लिखें और रिपलेस बटन पर क्लिक करें। यह डोक्यमेंट में सभी जगह रामेश को रामेश को बदल देगा।

स्पेल चेक विशेषता भाषा त्रुटियों को जाँचने में मदद करती है। इस्पेल चेक टैब में बैक्वार्ड्स और ली जैसे अप्शन्स होते हैं। इंग्लिश यूएसे भाषा के लिए स्पेल चेक करने के लिए टैब में इंग्लिश यूएसे चुनें और फिर डाउन एरोपर पर क्लिक करें। इस प्रकार डोक्यमेंट में इंग्लिश यूएसे भाषा का उपयोग करने में मदद मिलेगी।
>>>

SUMMARY G-W18-2:
<<<
इस ट्यूटोरियल में हम लिबर ऑफिस राइटर में फाइंड और रिप्लेस और स्पेलचेक विशेषताओं का इस्तेमाल सीखते हैं। फाइंड और रिप्लेस बटन क्लिक करके एक डायलॉग बॉक्स खोल सकते हैं जहाँ हम खोजने और बदलने का टेक्स्ट प्रविष्ट कर सकते हैं। सभी जगह खोजने के लिए 'अल्ल फाइंड अल्ल' और बदलने के लिए 'अल्ल रिप्लेस अल्ल' बटन क्लिक करें। स्पेलचेक त्रुटियों को जाँचने के लिए टूलबार में 'ऑटो स्पेलचेक' बटन क्लिक करें। यदि त्रुटियाँ होती हैं, उन्हें उपयोगकर्ता कोश में जोड़ा जाता है। भाषा सेटिंग्स बदलकर अंग्रेज़ी अमेरिका की भाषा चुनकर स्पेलचेक करें।
>>>

SUMMARY G-W18-3:
<<<
This tutorial explains how to use the "Find and Replace" feature in LibreOffice Writer, along with the "Spell Check" feature. To start, you open your document and click on the "Edit" option, then select "Find and Replace." This opens a dialog box where you can enter the text to find in the "Search for" field and the replacement text in the "Replace with" field. Clicking "All Find All" highlights all instances of the searched text, and clicking "All Replace All" replaces them with the new text. Advanced options like "Backwards," "Current Selection Only," and "Regular Expressions" are available for more complex searches.

For spell checking, you navigate to the "Tools" menu, then "Options," and set the language to English (USA) under the "Language Settings." This ensures the spell checker uses the correct dictionary. You can then enable auto-spell check from the toolbar. If it's not enabled, you can test it by typing a misspelled word like "husewife" instead of "housewife" in your document and pressing space. The spell checker will highlight the error and suggest corrections or add the word to your personal dictionary.
>>>

SUMMARY G-W18-4:
<<<
लिबर ऑफिस राइटर में फाइंड और रिप्लेस और ऑटोकरेक्ट विशेषताओं का इस्तेमाल सीखेंगे। फाइंड और रिप्लेस बटन क्लिक करके खोज और बदलने की विभिन्न विधियां सीखेंगे। उदाहरण के लिए, रमेश को मनीष से बदलने के लिए फाइंड फील्ड में रमेश लिखें, फिर फाइंड अल्ल बटन क्लिक करें। फिर रिप्लेस फील्ड में मनीष लिखें और रिप्लेस अल्ल बटन क्लिक करें। अधिक विशिष्ट विकल्पों के लिए, मोर ऑप्शन्स बटन क्लिक करें। यहां विशिष्ट खोज और बदलने के विकल्प दिखाई देते हैं।

स्पेल चेक भी सीखेंगे। टूल्बार में अटो स्पेल चेक बटन क्लिक करें। यदि यह निकटतम भाषा नहीं है, तो टूलबार में लिंक्स चुनें, फिर टूल्स में ऑप्शन्स चुनें, और फिर भाषा सेटिंग्स में इंग्लिश यूएसए चुनें। इस प्रकार स्पेल चेक विशेषता इंग्लिश यूएसए भाषा के लिए काम करेगी।
>>>

Reply with 4 lines, each with exactly 11 digits.
```

## Window W19 (12 facts, 4 summaries)

```
FACTS:
1. A newsletter is a publication distributed to subscribers at regular intervals, containing multiple columns to facilitate reading articles.
2. A new text document can be opened by clicking File, New, and then Text Document.
3. Columns are added to a document by clicking Format on the menu bar and selecting Columns.
4. The columns dialog box allows setting the number, width, spacing, and separator line properties of the columns.
5. Setting the value of the columns field to 2 creates two columns in the text area.
6. When typing reaches the end of the first column, the cursor automatically advances to the next column.
7. Pictures can be inserted and resized to properly fit inside a column.
8. A manual column break is inserted by clicking Insert, selecting Manual Break, choosing Column break, and clicking OK.
9. Selecting Green 4 from the background color icon changes the background of selected text to light green.
10. Banners can be added to the document by selecting the Text option from the Drawing toolbar and placing a text box.
11. Text animation options can be accessed by right-clicking the text and selecting Text from the context menu.
12. Selecting the Blink effect from the Text Animation tab causes the text to flash.

SUMMARY G-W19-1:
<<<
लिबर अफिस राइटर में सुशना पत्र बनाने की टिप्स इस ट्यूटरियल में सिखेंगे। यहां जेन्यू लिनक्स और लिबर अपने सुथ वर्जन 3.3.4 का उपयोग कर रहे हैं। सुशना पत्र एक प्रचारित रूप है जो ग्रहकों को समय के नियमित अन्तराल पर प्रचारित करता है। इसमें कई कोलंम्स होते हैं जो लेखों को आसान बनाते हैं। लिबर अफिस राइटर का उपयोग करके कोई भी सुशना पत्र बना सकता है जो लेखों का प्रचार बहुत सरल बनाता है। डालोग बॉक्स के माध्यम से कोलंम्स चुनें और उनकी विशेषताओं को सेट करें। फोरमेड बटन पर क्लिक करें और फिर कोलंम्स पर क्लिक करें। टेक्स्ट इन पर लिखें और नए कोलंम्स में टेक्स्ट जाने के लिए इंसर्ट बटन और मैनुअल ब्रेक बटन का उपयोग करें। टेक्स्ट के रंग और पृष्ठभूमि रंग बदलने के लिए बैग्रांड कलर और बैग्रांड अप्ट्टिन्स का उपयोग करें। टेक्स्ट अनिमेशन और ब्लिंग अप्ट्टिन्स भी उपलब्ध हैं।
>>>

SUMMARY G-W19-2:
<<<
लिबर ऑफिस राइटर में सूचना पत्र बनाने की विधि सिखेंगे। पहले नए text document खोलें और इसे newsletter नाम से save करें। फिर format बटन पर क्लिक कर और columns चुनें। दिए गए options से अंतराल और विभाजन निर्धारित करें। दो columns चुनें और उनकी विशेषताएं निर्धारित करें। पहले column में शीर्षक लिखें और दूसरे में लेख लिखें। दूसरे column में चित्र भी जोड़ सकते हैं। फिर नए column में लेख लिखें। अंत में ड्रॉइंग टूलबार का उपयोग कर बैनर जोड़ सकते हैं। टेक्स्ट ऑप्शन पर क्लिक कर टेक्स्ट बॉक्स बनाएं और इसमें टेक्स्ट लिखें। टेक्स्ट के उपर फील्ड में विभिन्न पृष्ठभूमि रंग और अन्य विशेषताएं जोड़ सकते हैं। टेक्स्ट को जगमगाने के लिए भी फील्ड में ब्लिंक ऑप्शन पर क्लिक करें।
>>>

SUMMARY G-W19-3:
<<<
LibreOffice Writer में सूचनापत्र बनाने की एक शिक्षा है। आप नए text document खोल सकते हैं और फिर format में columns चुनकर दो या तीन बार्ड को बनाएं। दृश्य में दो बार्ड दिखाई देते हैं। आप बार्ड के शीर्षक और लेख लिख सकते हैं। बार्ड के बीच विभाजक रेखा भी जोड़ सकते हैं। आप दूसरे बार्ड में नए लेख लिख सकते हैं। आप भूमिरंग और अन्य फॉर्मेटिंग विशेषताओं को लागू कर सकते हैं। आप बनाई गई बार्ड में बनावट जोड़ सकते हैं और भी विशेषताएँ जोड़ सकते हैं। उदाहरण के लिए, आप बार्ड के भाग को चुनकर पृष्ठभूमी रंग लागू कर सकते हैं। आप भी text box जोड़ सकते हैं और वहाँ लेख लिख सकते हैं। आप लेख को जगमगाने या अन्य प्रभावों से भी भर सकते हैं।
>>>

SUMMARY G-W19-4:
<<<
This tutorial explains how to create newsletters using LibreOffice Writer, a tool for organizing information into multiple columns. First, open a new text document and name it "newsletter." To add columns, click on the Format button, then Columns, which opens a dialog box where you can choose the number of columns, set their width and spacing, and select a separator line style. For a two-column layout, set the column count to 2 and choose a suitable format. You can then write content in each column, with the cursor automatically moving to the next column after finishing one. Insert breaks between columns by clicking Insert > Manual Break > Column Break. Formatting options like aligning text, changing background colors, and applying text effects are available. You can also add text boxes and banners to the newsletter. Effects such as blinking text can be applied to enhance the visual appeal.
>>>

Reply with 4 lines, each with exactly 12 digits.
```

## Window W20 (10 facts, 4 summaries)

```
FACTS:
1. Presentations cannot be edited while in slide show mode.
2. The F5 function key can be used to start a slide show.
3. Pressing the escape button exits the slide show.
4. The mouse pointer as pen option allows users to draw and write on the presentation during slide show mode.
5. Pressing the space bar advances the presentation to the next slide.
6. Slide transitions are visual effects applied when moving from one slide to another in a presentation.
7. Clicking on the Slide Sorter tab displays all slides in the presentation.
8. Slides can be rearranged by dragging and dropping a selected slide to a new position.
9. Transitions can be applied to slides by selecting slide transitions in the task pane.
10. Transition speed can be adjusted by selecting an option from the speed dropdown menu.

SUMMARY G-W20-1:
<<<
लिबर ऑफिस इम्प्रेस में स्लाइड शो बनाने के लिए आपको पहले इम्प्रेस डॉट ओडीपी खोलना होगा। फिर मुख्य मेनू से स्लाइड शो और स्लाइड शो सेटिंग्स पर क्लिक करें। आप दर्शकों को स्लाइड्स प्रस्तुत करने के लिए स्लाइड शो बनाएंगे। दाएं क्लिक करके अगले स्लाइड जाएंगे और दाएं क्लिक करके स्लाइड शो से बाहर आ सकते हैं। माउस पॉइंटर को पेन बनाने के लिए स्लाइड शो सेटिंग्स में चेक करें। इसे लगाने के लिए ऑप्शन्स के नीचे माउस पॉइंटर और माउस पॉइंटर को पेन बनाने के दो चेक बॉक्स को चेक करें। फिर स्लाइड शो में चेक करें और कर्सर पेन में बदल जाएगा। दाएं माउस बटन दबाकर रेखाएं बना सकते हैं। स्लाइड ट्रांजीशन्स के लिए टास्क पैन में स्लाइड ट्रांजीशन्स पर क्लिक करें और विभिन्न ट्रांजीशन्स और उनकी गति और ध्वनि को सेट कर सकते हैं।
>>>

SUMMARY G-W20-2:
<<<
लिबर अफिस में स्लाइड बनाने के लिए आप कीबोर्ड का उपयोग कर सकते हैं। नेविगेशन बरों का उपयोग करके आप नविगेट कर सकते हैं। अगली स्लाइड जाने के लिए कोंटेक्स्ट मेन्यू या डाया क्लिक करें। दर्शकों से बातचीत करने के लिए माउस पोइंटर दबाएं। स्लाइड शो सेटिंग्स में चुनें और स्लाइड शो बॉक्स पर क्लिक करें। दर्शकों से बातचीत करने के लिए इस विकल्प को सक्षम करें। ट्रन्दिशन्स बदलने के लिए मेन्यू से स्लाइड शो सेटिंग्स पर क्लिक करें और निस्लिट चुनें। निस्लिट निस्लिट स्पर्क्लिक करें और ट्रन्दिशन प्रभाव पैन में देखें। ड्राग और ड्रोप करके स्लाइड बदल सकते हैं। ट्रन्दिशन की गति नियन्त्रित करने के लिए इंप्रस लाइन ड्राब्डोन में चुनें।
>>>

SUMMARY G-W20-3:
<<<
This tutorial covers creating and presenting slides using LibreOffice Impress. You can create slide shows for presentations on desktops or projectors, which cover the entire screen. Slide shows are for presentation purposes only and cannot be edited while in show mode. To start a slide show, you can click on the "Slide Show" option in the main menu or press F5. During the show, you can navigate between slides using arrow keys or right-click the context menu to go to the next slide or choose "End Show." Alternatively, pressing the escape key also exits the slide show.

The tutorial explains how to use the mouse pointer as a pen to annotate slides during the presentation. This feature can be enabled by checking the "Mouse Pointer Visible" and "Mouse Pointer as Pen" boxes in the slide show settings dialog box. You can draw lines and add text on the slides when in slide show mode.

The tutorial also covers slide transitions, which are visual effects applied when moving from one slide to another. To change the order of slides, select the "Slide Sorter" tab and drag and drop slides. For applying transitions, select the desired slide, click on "Slide Transitions," and choose an effect like "Wipe Up." You can adjust the speed and add sound effects for each transition.
>>>

SUMMARY G-W20-4:
<<<
LibreOffice Impress में slide बनाने का ट्रायल करेंगे। आप slide shows और transitions बना सकते हैं जो दर्शकों के सामने प्रदर्शित होते हैं। इसके लिए आप main menu से slide show चुनें और settings पर click करें। या फिर F5 फंक्शन की तरफ जाकर slide show शुरू कर सकते हैं। दर्शकों के सामने slide प्रस्तुत करने के लिए arrow buttons का उपयोग करें या context menu के लिए दायां click करें। यदि आप चाहते हैं कि दर्शकों से बातचीत करें, mouse pointer को pen बनाएँ। इसके लिए slide show settings में mouse pointer visible और pen चेक करें। फिर कुछ चित्र बनाने के लिए sketch pen चुनें। यदि आप चाहते हैं कि दूसरी slide पर जाएँ, space bar दबाएँ। यदि आप चाहते हैं कि slide show से बाहर आएँ, दायां click करें और end show चुनें। या फिर escape button दबाएँ। slide transitions बनाने के लिए slide sorter टैब पर click करें और transitions चुनें। उन्हें speed और sound से नियंत्रित कर सकते हैं।
>>>

Reply with 4 lines, each with exactly 10 digits.
```

## Window W21 (10 facts, 4 summaries)

```
FACTS:
1. A presentation can be printed by selecting File then Print or by pressing the Ctrl and P keys together.
2. Under the Document field in the General tab, available presentation print options include slides, handouts, notes, and outline.
3. In the LibreOffice Impress tab under Content, users can choose to print the slide name, date and time, and hidden pages.
4. Selecting the draw a border around each page option creates a black border around each printed page.
5. The brochure option formats slides to be printed as a booklet suitable for binding.
6. The default handout configuration places four slides per page ordered from left to right and then down.
7. Size options under the LibreOffice Impress tab are disabled when printing handouts because print size is determined by sheet size and slide count.
8. Notes for a slide can be added by navigating to the slide and clicking the Notes tab.
9. Selecting notes under the Document field displays typed slide notes at the bottom of the slide in the print preview.
10. Size options in the LibreOffice Impress tab are unavailable when printing notes.

SUMMARY G-W21-1:
<<<
इस ट्यूटोरियल में दिए गए हैं लिबरऑफिस इम्प्रेस में प्रस्तुति को प्रिंट करने के विभिन्न विकल्प। पहले आपको प्रस्तुति खोलना है, फिर फाइल में प्रिंट चुनिए या Ctrl+P दबाएं। जनरल और ऑप्शन्स टैब में आप विभिन्न प्रिंट विकल्प देख सकते हैं। आप स्लाइड, हैण्डआउट्स, नोट्स और ऑटलाइन चुन सकते हैं। आप स्लाइड के रंग, आकार और कॉलर फॉर्मेट भी निर्धारित कर सकते हैं। पेज लायアウト टैब में आप एक पेज पर कितने स्लाइड प्रिंट करना चाहते हैं और एक पेज पर कितने स्लाइड देखना चाहते हैं। नोट्स टैब पर जाकर आप नोट्स प्रिंट कर सकते हैं लेकिन उसके लिए आपको आर्किटेक्चर विकल्प नहीं मिलेंगे। अंत में प्रिंट बटन पर क्लिक करके प्रिंट करें।
>>>

SUMMARY G-W21-2:
<<<
लिबर ऑफिस इम्प्रेस में प्रस्तुति को प्रिंट करने के लिए दो प्रकार के ऑप्शन हैं: स्लाइड्स और हैंडआउट्स। स्लाइड्स को प्रिंट करने के लिए फाइल और प्रिंट या कंट्रोल और पी कीज करें। लिबर ऑफिस इम्प्रेस टैब में स्लाइड के रंग, आकार और अन्य विवरण निर्धारित किए जा सकते हैं। ऑप्शन में डिफॉल्ट, ग्रेस्केल और फिट टू प्रिन्टेबल पेज शामिल हैं। हैंडआउट्स को प्रिंट करने के लिए फाइल और प्रिंट या कंट्रोल और पी कीज करें। दूसरे ऑप्शन में पेज लाइट्यूट और ब्राउजर शामिल हैं। नोट्स को प्रिंट करने के लिए नोट्स टैब पर जाकर टाइप किए गए नोट्स प्रिंट होने के लिए फाइल और प्रिंट या कंट्रोल और पी कीज करें।
>>>

SUMMARY G-W21-3:
<<<
This tutorial explains how to print presentations in LibreOffice Impress, using GNU/Linux as the operating system and version 3.3.4 of LibreOffice. To print slides, you can open your presentation, then go to File > Print or use Ctrl+P. In the General and Options tabs, you can choose specific options for printing slides, such as including slide names, dates, and hidden pages in grayscale or color. You can also select how many slides to print per page and customize the layout. For handouts, choose Handout from the Document field in the Print section, which defaults to four slides per page. Notes can be printed by selecting Notes from the Document field in the Print section, though fewer customization options are available. Finally, clicking the Print button will start the printing process if the printer is correctly configured.
>>>

SUMMARY G-W21-4:
<<<
लिबर अफिस में प्रस्तुती को प्रि�ंट करने के लिए आपको पहले अपनी प्रस्तुती सैंपल इंप्रस पर खिलकर उसे खोलते हैं। फिर फिल और प्रिंट टैब पर क्लिक करके प्रिंट लेने की विभिन्न विकल्पों को देखते हैं। जनरल टाब में प्रिंट के अंदर दोक्यमेंस फील में अप्टिन्स देखते हैं। आप अपनी सलिट्स को चुनकर चार स्लाइट्स प्रिंट कर सकते हैं। आप अपने सलिट्स के भागों को कलर, साइस और चुनाउ कर सकते हैं। यदि आपकी प्रस्तुती को एक पेज पर दो स्लाइट्स चाहिए, तो आप दो पेज पर एक स्लाइट प्रिंट कर सकते हैं। ब्राउशर अप्टिन्स भी उपलब्ध हैं जो बाइन्टिंग के लिए अच्छी तरह से उपयोगी होते हैं। अंत में, आप प्रिंट बटन पर क्लिक करके प्रिंट करते हैं। यदि आपकी प्रस्तुती को नोट्स या नोट्स प्रिंट करना चाहते हैं, तो आप नोट्स अप्टिन्स चुनकर नोट्स प्रिंट कर सकते हैं।
>>>

Reply with 4 lines, each with exactly 10 digits.
```

## Window W22 (10 facts, 4 summaries)

```
FACTS:
1. The terminal can be opened by simultaneously pressing the Ctrl, Alt, and T keys.
2. JChemPaint preferences can be accessed through the Edit menu.
3. The choose background color window contains tabs labeled Swatches, HSB, and RGB.
4. The Windows operating system provides two extra tabs named HSL and CMYK for color selection.
5. The Look and Feel section dropdown includes options for System, Metal, Nimbus, Motif, GTK, and Windows.
6. The user interface language dropdown includes American English alongside other languages.
7. American English is chosen as the default user interface language.
8. Modifying the user interface language changes the text on the menu bar and status bar.
9. The templates menu tool can alternatively be accessed from the side toolbar.
10. Clicking the All Templates tab opens the structure templates window displaying templates with their structures.

SUMMARY G-W22-1:
<<<
नमस्कार, जे कैंपेंट के टोटोरियल में आपका स्वागत है। यहाँ आपको बताना है कि जे कैंपेंट विंडो का बैकग्राउंड रंग और यूजर इंटरफेस भाषा कैसे तय किया जाता है। बैकग्राउंड रंग तय करने के लिए, पहले डेस्कटॉप पर डॉट जार फाइल खोलें, फिर टर्मिनल में `java -jar jcampaign-3.3.1210.jar` टाइप करें और एंटर दबाएं। फिर `Edit` मेनू से `Preferences` चलें और `jCampaign Preferences` विंडो में जाएं। बैकग्राउंड कलर बटन पर क्लिक करें और चुनित रंग को चुनें। अन्य पREFERENCE टैब पर जाएं और `Look and Feel` क्षेत्र में चुनित विंडो दिखावट को लागू करें। यूजर इंटरफेस भाषा भी तय कर सकते हैं, इसके लिए `Edit` मेनू से `Preferences` चलें और `Other Preferences` टैब पर जाएं। यहाँ भाषा ड्रॉपडाउन सूची में चुनित भाषा को लागू करें। फिर टेम्पलेट्स सम्मिलित करने के लिए, `Templates` मेनू खोलें या वाइड टूलबार से खोलें। `All Templates` टैब पर जाएं और विंडो टेम्पलेट्स विंडो में देखें।
>>>

SUMMARY G-W22-2:
<<<
नमस्कार, फीट्चर्स अफ जे केंपेंट के टोटर्यल में आप निम्न करने की जानकारी मिलेगी: पैनल का बैक्राउन रंग बिन्डो कैसे करें, यूसर इंट्रफेज भाषा बदलें, तेमपलेट्स सम्मिलित करें, इस्टॉक्तर्स बनाएं, और इस्टॉटर्याल लिकोड करें। जे केंपेंट विन्डो खोलने के लिए कंट्रोल ओल्ट + ती कीस दवाएं लिखें। पैनल का रंग बदलने के लिए प्रेफ्रेंशिस विन्डो खोलें और जूस बेग्राउन कलार बटन पर क्लिक करें। यूसर इंट्रफेज बदलने के लिए प्रेफ्रेंशिस टैप पर क्लिक करें और लुक अन फील चेत्र में अमेरिकन इंगलिश चुनें। तेमपलेट्स सम्मिलित करने के लिए मैनिव पर क्लिक करें और तेमपलेट्स द्रोब्डान खोलें। इस्टॉक्तर्स बनाने के लिए तेमपलेट्स ताप पर क्लिक करें और इस्ट्रक्चर ताम्पलेट्स विन्डो खोलें।
>>>

SUMMARY G-W22-3:
<<<
नमस्कार, जेकेम्पे�int के इस ट्यूटोरियल में हम निम्न करेंगे: पैनल का रंग बदलना, उज़र इंटरफेस भाषा बदलना, और टेम्पलेट और स्ट्रक्चर्स बनाना। पैनल का रंग बदलने के लिए, हम एडिट मेनू से पREFERENCE करते हैं, फिर बैकग्राउंड रंग चुनते हैं। उज़र इंटरफेस भाषा बदलने के लिए, हम EDIT मेनू से पREFERENCE करते हैं, फिर USER INTERFACE LANGUAGE चुनते हैं। टेम्पलेट और स्ट्रक्चर्स बनाने के लिए, हम टेम्पलेट मेनू से टेम्पलेट चुनते हैं या ओर ओवरलैट बार से टेम्पलेट चुनते हैं।
>>>

SUMMARY G-W22-4:
<<<
This tutorial covers how to customize the JChemPaint software, a chemical structures editor. It starts by opening the JChemPaint window on Ubuntu Linux OS version 12.04 with JChemPaint version 3.31210 and Java version 7. Key steps include changing the panel background color through the Preferences menu, selecting from various color options including HSB, RGB, and others depending on your operating system. The tutorial also explains how to change the user interface language to Spanish or other languages available in the Other Preferences tab. Additionally, it demonstrates adding templates to the software by navigating to the Templates menu or using the side toolbar, and viewing the list of available structure templates in the Structure Templates window.
>>>

Reply with 4 lines, each with exactly 10 digits.
```

## Window W23 (11 facts, 4 summaries)

```
FACTS:
1. LibreOffice Impress opens in Normal view by default.
2. Users can return to Normal view by clicking the Normal tab or selecting View and then Normal.
3. Slides can be created and edited in Normal view.
4. Slide designs can be selected and changed from the Master Pages section of the Tasks pane.
5. Outline view arranges slide contents sequentially below one another like a table.
6. Outline view allows rearranging line items by moving them up, down, or across lines.
7. Slide Sorter view is used to sort slides into any desired sequence.
8. Notes view allows presenters to write speaker notes to assist them during a presentation.
9. Notes written in Notes view remain visible to the presenter on the monitor but hidden from the audience.
10. The Tasks pane can be displayed or hidden by clicking View and selecting Tasks Pane.
11. The slide layout can be changed using the Layout section in the Tasks pane.

SUMMARY G-W23-1:
<<<
लिबर ऑफिस इंप्रेस में देखने के लिए ट्यूटोरियल में आपका स्वागत है। हम व्यू ऑप्शन्स और उनके उपयोग और मास्टर पेजेस के बारे में सीखेंगे। इस ट्यूटोरियल में हम ग्नु लिनुक्स और लिबर ऑफिस वर्सन 334 का उपयोग कर रहे हैं। पहले हम अपनी प्रस्तुति सानप्लेस इंप्रेस खोलते हैं। लिबर ऑफिस इंप्रेस में विभिन्न व्यू ऑप्शन्स हैं जो आपको अच्छी प्रस्तुति बनाने में मदद करते हैं। डेफैल्ट में नॉर्मल व्यू दिखता है, जब आप लिबर ऑफिस इंप्रेस शुरू करते हैं। आप नॉर्मल टैब पर क्लिक करके या व्यू और नॉर्मल पर क्लिक करके नॉर्मल व्यू में वापस आ सकते हैं। आउटलाइन व्यू में आप स्लाइड कंटेंट्स के रूप में एक व्यवस्थित रूप में देख सकते हैं। नॉर्मल व्यू में आप डिजाइन्स जोड़ सकते हैं और लेआउट बदल सकते हैं। नोट्स व्यू में आप नोट्स लिख सकते हैं जो आपकी प्रस्तुति के समय मदद करेंगे। अंत में, हम एक नए मास्टर पेज बनाने की कोशिश करेंगे जो डार्क ब्लू बैकग्राउंड और लाइट ब्लू टाइटल क्षेत्र वाला हो।
>>>

SUMMARY G-W23-2:
<<<
लिबर अफिस इंप्रस में प्रस्तुती लेखने के लिए आपका स्वागत है। यहां हम नोर्मल व्यु, स्लाइट्स और मास्टर पेजेंस के बारे में सीखेंगे। नोर्मल व्यु में आप अपनी प्रस्तुती कर सकते हैं। स्लाइट्स बनाने के लिए आप अट्लान टैप क्लिक कर सकते हैं। बूलेट पौएंट और बूलेट पौएंट बड़ाने के लिए लाईन अटम्स और लाईन कुन्त्रोल अज्द इस्तेमाल कर सकते हैं। नोट्स लिखने के लिए नोट्स पेजबर इस्तेमाल करें। स्लाइट सोटर इस्तेमाल करके स्लाइट्स को सोटा या वापस ले सकते हैं। देवलप्मेंट लियाउट इस्तेमाल करके स्लाइट के लिए नया लॉट्स बना सकते हैं। यहां तक कि एक ब्लु बेग्राउन और लाइट ब्लु टाट्र के साथ एक मास्टर पेज बनाने के लिए भी आपको सीखना पड़ेगा।
>>>

SUMMARY G-W23-3:
<<<
This tutorial covers various view options in LibreOffice Impress, a presentation software. It starts with the default Normal view and explains how to switch between different views like Outline, Slide Sorter, and Notes. The tutorial demonstrates changing slide designs using the Master Pages feature, which can be accessed from the Tasks Pane. Users learn to rearrange slides, modify slide layouts, and adjust the presentation layout. Key features discussed include the Outline view for organizing slides, Slide Sorter for reordering slides, and Notes view for adding notes that appear on the presenter's screen but not the audience's. The tutorial also shows how to customize the background and title areas of slides using Master Pages. Overall, it guides users through creating a new presentation with a dark blue background and light blue title area, encouraging them to practice these skills.
>>>

SUMMARY G-W23-4:
<<<
लिबर ऑफिस इम प्रेस में प्रस्तुति देखने के लिए टीटूरियल में आपका स्वागत है। हम व्यू ऑप्शंस और उनके उपयोग और मास्टर पेजेस के बारे में सीखेंगे। इस टीटूरियल में हम ग्नु लिनुक्स और लिबर ऑफिस वर्जन थ्री थ्री फोर का उपयोग कर रहे हैं। पहले आपको अपनी प्रस्तुति सैंपल इम्प्रेस ओपन करना है। डिफॉल्ट नोर्मल व्यू में देखने के लिए नोर्मल टैब पर क्लिक करें। अन्य व्यू जैसे डिस्प्रेस व्यू और ऑलाइन व्यू में भी देखने के लिए व्यू और व्यू पेज पर क्लिक करें। मास्टर पेजेज सेक्शन में आप अपने प्रस्तुतियों के लिए विभिन्न डिज़ाइन देख सकते हैं। ऑलाइन व्यू में स्लाइड्स के कंटेंट टेबल की तरह व्यवस्थित होते हैं। नोट्स व्यू में नोट्स लिखने के लिए व्यू और नोट्स पेज पर क्लिक करें। मास्टर पेजेज बनाने के लिए निम्न लिंक पर जाएं।
>>>

Reply with 4 lines, each with exactly 11 digits.
```

## Window W24 (13 facts, 4 summaries)

```
FACTS:
1. The file block.fig is opened in Xfig and saved as feedback.fig using the Save As option.
2. Grids can be added to the drawing area by clicking on grids.
3. The functions of the mouse buttons are displayed in the upper right and vary depending on the current activity.
4. Clicking the left mouse button on the vertical scroll bar scrolls the canvas up, while the right mouse button scrolls it down.
5. The canvas can be moved up or down by clicking the middle mouse button and dragging.
6. The top scroll bar is used to navigate the canvas horizontally to the left or right.
7. A box is copied by clicking to select it, moving the cursor to a new location, and clicking again.
8. The text tool is selected by clicking the text box icon marked by 't' on the left panel.
9. The text font size is configured by entering 16 into the value box and clicking set.
10. Center alignment for text is chosen using the text justification button in the attribute panel.
11. The text "control" is entered in the center of the box.
12. The polyline button is chosen to insert lines with arrows.
13. Arrowhead settings are adjusted using the arrow mode button in the attribute panel.

SUMMARY G-W24-1:
<<<
ब्लोक्टाग्रम क्रीशन में ब्लोक स्टोरीज को चुरू करने से पहले ब्लोक स्टोरीज को अच्छी तरह से जानना महत्वपूर्ण है। ब्लोक टीटोरियल में बनाए गए ब्लोक्स को देखकर हम ब्लोक डोट पिक से शिरवात कर सकते हैं। ब्लोक्स टीटोरियल में एक स्विच पर चलते हैं और ब्लोक्स टीटोरियल में एक स्विच पर चलते हैं। यहाँ बाई वाटन की तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तरफ दाहिने तर
>>>

SUMMARY G-W24-2:
<<<
This tutorial explains how to create a feedback diagram using the software Xfig version 3.2 patch level 5. It starts with creating blocks using the `blockfig` command, which was previously used in the block tutorial. You open a file, enter the block name in the open entry box, and click open or double-click `blockfig`. Save the figure as "feedbackfig". To move the canvas, use the vertical scroll bar; the left mouse button moves it up, the right down, and the center button drags the canvas. For the horizontal scroll bar, left and right buttons move the canvas left and right, respectively. 

To create a feedback diagram, copy a block, place it somewhere else, and add text by clicking on the text box. Adjust the text size by dragging the value box to 16 and clicking set. Align the text to the center by clicking the appropriate button in the attributes panel. If you make a mistake, you can correct it by clicking elsewhere and then back to the correct position. Finally, add arrows and lines by selecting the polyline button, choosing arrow mode and type, and clicking on the arrow head.
>>>

SUMMARY G-W24-3:
<<<
इस ट्यूटोरियल में एक्सफिग का इस्तेमाल करके फीडबैक डाइअग्रैम बनाने की विधि सिखाई गई। पहले ब्लॉक्स ट्यूटोरियल को देखें, फिर एक फाइल चुनें और ब्लॉक एन्टर करें। फिर फीडबैक नाम से फाइल सेव करें। ग्रिड डालने के लिए ग्रिड्स पर क्लिक करें। कैनवास को ऊपर या नीचे ले जाने के लिए स्क्रोल बार का प्रयोग करें। माउस बटनों की भूमिका बदलने के लिए कैनवास पर क्लिक करें। फीडबैक बॉक्स को कॉपी करें, फिर नई जगह पर पट्टी डालें। टेक्स्ट बॉक्स में टेक्स्ट डालें, उसके बाद टेक्स्ट जस्टिफाइ करें। फिर एरो और पॉलीलाइन बटन का इस्तेमाल करके लाइन डालें।
>>>

SUMMARY G-W24-4:
<<<
इस टुटोरियल में हम फीडबैक डायग्राम कैसे बनाते हैं सिखते हैं। पहले हम xfig फ़ाइल में ब्लॉक डायग्राम क्रिएशन करते हैं। फिर file को open करते हैं और block को enter करते हैं। फीडबैक डायग्राम को feedback.dot fig नाम से save करते हैं। ग्रिड को चुनकर डालते हैं और mouse के बटनों का उपयोग करके डायग्राम को ऊपर या नीचे बढ़ाते हैं। middle button पर click करके और drag करके डायग्राम को केंद्र में लाते हैं। फिर डायग्राम को copy करते हैं और नई जगह पर पालटाते हैं। फिर text box को चुनकर टेक्स्ट डालते हैं और text size चुनते हैं। फिर polyline button को चुनकर और lines डालते हैं। arrow mode और arrow type बटन को चुनकर और arrow head को डालते हैं।
>>>

Reply with 4 lines, each with exactly 13 digits.
```
