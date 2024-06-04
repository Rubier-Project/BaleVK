import java.net.HttpURLConnection;
import java.net.URL;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class main {
    private String BotToken;

    public void setToken(String token){
        this.BotToken = token;
    }

    public String getBaleApi(){
        return "https://tapi.bale.ai/bot"+this.BotToken+"/";
    }

    public String makeTextBold(String text){
        return "*"+text+"*";
    }

    public String makeTextItalic(String text){
        return "_"+text+"_";
    }

    public String addLinkToText(String text, String link){
        return "["+text+"]"+"("+link+")";
    }

    public String addDetailsToText(String text, String details){
        return "```["+text+"]"+details+"```";
    }

    public String MakeRequest(String _url, String reqMethod) {
        try {
            URL url = new URL(_url);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod(reqMethod);

            BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            String inputLine;
            StringBuffer response = new StringBuffer();

            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();
            connection.disconnect();

            return response.toString();
        } catch (Exception e) {
            return e.getMessage();
        }
    }

    public String onUpdates(int limit, int offset){
        return MakeRequest(getBaleApi()+"getUpdates", "GET");
    }

    public String onChatUpdates(String chatID){
        return MakeRequest(getBaleApi()+"getChat?chat_id="+chatID, "GET");
    }

    public String sendMessage(String chatID, String text, 
                              String messageID){
                                return MakeRequest(getBaleApi()+"sendMessage?chat_id="+chatID+"&text="+text+"&reply_to_message_id="+messageID, "GET");
                              }

    public String getMe(){
        return MakeRequest(getBaleApi()+"getMe", "GET");
    }

    public String logout(){
        return MakeRequest(getBaleApi()+"logout", "GET");
    }

    public String close(){
        return MakeRequest(getBaleApi()+"close", "GET");
    }

    public String forwardMessage(String toChatID, String fromChatID, String messageID){
        return MakeRequest(getBaleApi()+"forwardMessage?chat_id="+toChatID+"&from_chat_id="+fromChatID+"&message_id="+messageID, "GET");
    }

    public String sendLocation(String chatID, String longitude, String latitude){
        return MakeRequest(getBaleApi()+"sendLocation?chat_id="+chatID+"&longitude="+longitude+"&latitude="+latitude, "GET");
    }

    public String sendContact(String chatID, String FirstName, String PhoneNumber){
        return MakeRequest(getBaleApi()+"sendContact?chat_id="+chatID+"&first_name="+FirstName+"&phone_number="+PhoneNumber, "GET");
    }

    public String getFile(String fileID){
        return MakeRequest(getBaleApi()+"getFile?file_id="+fileID, "GET");
    }

    public String banChatMember(String chatID, String userID){
        return MakeRequest(getBaleApi()+"banChatMember?chat_id="+chatID+"&user_id="+userID, "GET");
    }

    public String unbanChatMember(String chatID, String userID){
        return MakeRequest(getBaleApi()+"unbanChatMember?chat_id="+chatID+"&user_id="+userID, "GET");
    }

    public String promoteChatMember(String chatID, String userID){
        return MakeRequest(getBaleApi()+"promoteChatMember?chat_id="+chatID+"&user_id="+userID, "GET");
    }

    public String leaveChat(String chatID){
        return MakeRequest(getBaleApi()+"leaveChat?chat_id="+chatID, "GET");
    }

    public String getChatMemberCount(String chatID){
        return MakeRequest(getBaleApi()+"getChatMemberCount?chat_id="+chatID, "GET");
    }

    public String editMessageText(String chatID, String messageID, String newText){
        return MakeRequest(getBaleApi()+"editMessageText?chat_id="+chatID+"&text="+text+"&message_id="+messageID, "GET");
    }

    public String deleteMessage(String chatID, String messageID){
        return MakeRequest(getBaleApi()+"deleteMessage?chat_id="+chatID+"&message_id="+messageID, "GET");
    }
  
    // Example
    // public static void main(String[] args){
        // main m = new main();
        // m.setToken("123456789:aDUASIDdsaidIAUSOSDUIASDUISASOAHDASUDI");
        // System.out.println(m.getMe());
    }
}
