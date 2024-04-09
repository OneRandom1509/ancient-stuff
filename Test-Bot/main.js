const { Client, GatewayIntentBits } = require('discord.js');
const client = new Client({ intents: [GatewayIntentBits.Guilds] });
const commands = [
    {
        name: 'ping',
        description: 'Replies with Pong!',
    },
];
const { REST, Routes } = require('discord.js');
const rest = new REST({ version: '10'}).setToken('hehehe');


client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});


(async () => {
    try {
    console.log('Started refreshing application (/) commands.');

    await rest.put(Routes.applicationCommands('915992881171406859'), { body: commands });

    console.log('Successfully reloaded application (/) commands.');
    } catch (error) {
    console.error(error);
    }
})();
client.login('hehehe');