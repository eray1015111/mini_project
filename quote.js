var qoutearray=[
{
	"author":"Gojo Satoru",
	"quote":"Dying to win and risking death to win are completely different."
},
{
	"author":"Gojo Satoru",
	"quote":"Searching for someone to blame is just a pain."},
{
	"author":"Gojo Satoru",
	"quote":"But no matter how many allies you have around you, when you die, you’ll be alone."},
{
	"author":"Gojo Satoru",
	"quote":"I’ve always been a nice guy who cares for my students."},
{
	"author":"Megumi Fushigoro",
	"quote":"It’s not about whether I can, I have to do it."},
{
	"author":"Two Doors Cinema Club",
	"quote":"If you think of me, I will think of you."},
{
	"author":"Megumi Fushigoro",
	"quote":"I didn’t say to come back for it, I said to leave it behind."},
	{
	"author":"Megumi Fushigoro",
	"quote":"I want more people to enjoy fairness, even if only a few."},
	{
	"author":"Megumi Fushigoro",
	"quote":"I have no intention of risking my life to save someone I had no intention of saving in the first place."},
	{
	"author":"Megumi Fushigoro",
	"quote":"Only the unfair truth fairly distributes to all of us."},
	{
	"author":"Yuji Itadori",
	"quote":"I don’t know how I’ll feel when I’m dead, but I don’t want to regret the way I lived."},
	{
	"author":"Mahito",
	"quote":"You can’t let yourself get trapped in an ideal of indifference."},
	{
	"author":"Nanami",
	"quote":"The accumulation of those little despairs is what makes a person an adult."}

]
function randomselect(arrayLength){
	return Math.floor(Math.random()*arrayLength);
}
function generateQuote(){
	var randomnum=randomselect(qoutearray.length);
	document.getElementById("quoteOutput").innerHTML='"'+qoutearray[randomnum].quote+'"'
	document.getElementById("authorOutput").innerHTML='"'+qoutearray[randomnum].author+'"'
}