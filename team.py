
import asyncio

from agents.query_agent import analyse_customer_query
from agents.knowledge_agent import retrieve_knowledge
from agents.resolution_agent import generate_resolution
from agents.log_agent import create_ticket_log


async def run_customer_support(
    complaint: str,
    customer_name: str = "Not provided",
    order_id: str = "Not provided"
) -> dict:

    print("\n" + "=" * 60)
    print("SHOPEASE AI CUSTOMER SUPPORT WORKFLOW")
    print("=" * 60)

    # AGENT 1: Customer Query Agent
    print("\n[1/4] Customer Query Agent is analysing the complaint...")

    query_analysis = await analyse_customer_query(complaint)

    print("\nQUERY ANALYSIS:")
    print(query_analysis)

    # AGENT 2: Knowledge Base Agent
    print("\n[2/4] Knowledge Base Agent is searching FAISS...")

    knowledge_results = await retrieve_knowledge(
        complaint + "\n" + query_analysis
    )

    print("\nKNOWLEDGE BASE RESULTS:")
    print(knowledge_results)

    # AGENT 3: Resolution Agent
    print("\n[3/4] Resolution Agent is preparing the response...")

    resolution = await generate_resolution(
        customer_complaint=complaint,
        query_analysis=query_analysis,
        knowledge_results=knowledge_results
    )

    print("\nCUSTOMER RESPONSE:")
    print(resolution)

    # AGENT 4: Log Agent
    print("\n[4/4] Log Agent is creating the ticket...")

    ticket = create_ticket_log(
        customer_complaint=complaint,
        query_analysis=query_analysis,
        knowledge_results=knowledge_results,
        resolution=resolution,
        customer_name=customer_name,
        order_id=order_id
    )

    print("\nTICKET INFORMATION:")
    print(f"Ticket ID: {ticket['ticket_id']}")
    print(f"Category: {ticket['category']}")
    print(f"Urgency: {ticket['urgency']}")
    print(f"Sentiment: {ticket['sentiment']}")
    print(f"Status: {ticket['status']}")
    print(f"Escalation Reason: {ticket['escalation_reason']}")

    print("\n" + "=" * 60)
    print("CUSTOMER SUPPORT WORKFLOW COMPLETED")
    print("=" * 60)

    return {
        "query_analysis": query_analysis,
        "knowledge_results": knowledge_results,
        "resolution": resolution,
        "ticket": ticket
    }


if __name__ == "__main__":

    sample_complaint = (
        "I received my product three days ago and want to "
        "request a refund. The product is unused and in "
        "its original packaging."
    )

    result = asyncio.run(
        run_customer_support(
            complaint=sample_complaint,
            customer_name="Test Customer",
            order_id="ORD-2001"
        )
    )
