//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
import java.io.*;
import java.util.HashMap;
import java.util.Map;
import org.json.JSONObject;



public class Main {
    public static void main(String[] args) {
        String filepath;

//        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
//
//            filepath = br.readLine();
//            System.out.println(filepath);
//        } catch (IOException e) {
//            System.err.println("Error reading input: " + e.getMessage());
//            return;
//        }

        StringBuilder contentBuilder = new StringBuilder();
        try (BufferedReader fileReader = new BufferedReader(new InputStreamReader(System.in))) {
            String line;
            while ((line = fileReader.readLine()) != null) {
                contentBuilder.append(line).append("\n");
            }
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
            return;
        }

        String content = contentBuilder.toString();
        Statistics stats = new Statistics();
        stats.analyzeFile(content);
        JSONObject jsonStats = stats.toJson();
        System.out.println(jsonStats.toString());
    }
}

class Statistics {
    String filepath;
    int totalCharacters;
    int totalWords;
    int totalLines;
    char mostCommonCharacter;
    String mostCommonWord;

//    public Statistics(String filepath) {
//        this.filepath = filepath;
//    }

    public void analyzeFile(String content) {
        // Counting characters
        totalCharacters = content.length();

        // Counting words
        String[] words = content.trim().split("\\s+");
        totalWords = words.length;

        // Counting lines
        totalLines = content.split("\r\n|\r|\n").length;

        // Counting most common character
        Map<Character, Integer> characterCounts = new HashMap<>();
        for (char c : content.toCharArray()) {
            if (Character.isLetter(c)) {
                characterCounts.put(c, characterCounts.getOrDefault(c, 0) + 1);
            }
        }
        mostCommonCharacter = characterCounts.entrySet().stream()
                .max(Map.Entry.comparingByValue())
                .map(Map.Entry::getKey)
                .orElse(' ');

        // Counting most common word
        Map<String, Integer> wordCounts = new HashMap<>();
        for (String word : words) {
            wordCounts.put(word, wordCounts.getOrDefault(word, 0) + 1);
        }
        mostCommonWord = wordCounts.entrySet().stream()
                .max(Map.Entry.comparingByValue())
                .map(Map.Entry::getKey)
                .orElse("");
    }

    public JSONObject toJson() {
        JSONObject json = new JSONObject();
        json.put("filepath", filepath);
        json.put("totalCharacters", totalCharacters);
        json.put("totalWords", totalWords);
        json.put("totalLines", totalLines);
        json.put("mostCommonCharacter", mostCommonCharacter);
        json.put("mostCommonWord", mostCommonWord);
        return json;
    }
};
