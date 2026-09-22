import "dotenv/config";
import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
import { ChatOpenAI } from "@langchain/openai";

const model = new ChatOpenAI({
  modelName: "auto", // Let the proxy auto-route to the best available provider
  temperature: 0.7,
  apiKey: process.env.FREELLMAPI_KEY, // The unified freellmapi-... token
  configuration: {
    baseURL: "http://localhost:3001/v1",
  },
});

async function main() {
  const rl = readline.createInterface({ input, output });

  try {
    while (true) {
      const userPrompt = await rl.question("Enter your prompt (or 'exit' to quit): ");
      if (userPrompt.trim().toLowerCase() === "exit") break;

      const stream = await model.stream(userPrompt);

      process.stdout.write("\nResponse: ");
      for await (const chunk of stream) {
        process.stdout.write(chunk.content);
      }
      process.stdout.write("\n\n");
    }
  } catch (err) {
    console.error("Execution error:", err.message || err);
  } finally {
    rl.close();
  }
}

main();